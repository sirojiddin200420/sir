import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 12 viloyat (Toshkent shahri alohida emas)
VILOYATLAR = {
    "Andijon": (40.7829, 72.3442),
    "Buxoro": (39.7670, 64.4230),
    "Farg‘ona": (40.3894, 71.7843),
    "Jizzax": (40.1250, 67.8800),
    "Xorazm (Urganch)": (41.5500, 60.6333),
    "Namangan": (40.9983, 71.6726),
    "Navoiy": (40.0844, 65.3792),
    "Qashqadaryo (Qarshi)": (38.8610, 65.7847),
    "Samarqand": (39.6542, 66.9597),
    "Sirdaryo (Guliston)": (40.4897, 68.7842),
    "Surxondaryo (Termiz)": (37.2242, 67.2783),
    "Toshkent viloyati (Nurafshon)": (41.0230, 69.3380),
}

TIMEZONE = "Asia/Tashkent"
DAYS = 7

OUT_DIR = "weather_out"
IMG_DIR = os.path.join(OUT_DIR, "img")
CSV_DIR = os.path.join(OUT_DIR, "csv")
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(CSV_DIR, exist_ok=True)

def fetch_weather(lat: float, lon: float) -> pd.DataFrame:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&forecast_days={DAYS}"
        f"&timezone={TIMEZONE}"
    )
    r = requests.get(url, timeout=25)
    r.raise_for_status()
    data = r.json()

    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "tmax": data["daily"]["temperature_2m_max"],
        "tmin": data["daily"]["temperature_2m_min"],
    })
    return df

def plot_weather(df: pd.DataFrame, title: str, out_path: str):
    plt.figure(figsize=(10, 4))
    plt.bar(df["date"], df["tmax"], label="Max (°C)")
    plt.bar(df["date"], df["tmin"], label="Min (°C)")
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.xlabel("Sana")
    plt.ylabel("Harorat °C")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()

def df_to_html_table(df: pd.DataFrame) -> str:
    nice = df.rename(columns={"date": "Sana", "tmax": "Max °C", "tmin": "Min °C"})
    return nice.to_html(index=False, border=0)

html_parts = []
html_parts.append("""<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>O‘zbekiston: 12 viloyat ob-havo (7 kun)</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 24px; background: #fafafa; }
    h1 { margin-bottom: 6px; }
    .subtitle { color: #555; margin-top: 0; }
    .grid { display: grid; grid-template-columns: 1fr; gap: 18px; }
    .card { background: white; border: 1px solid #e6e6e6; border-radius: 12px; padding: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.04); }
    figure { margin: 12px 0 10px; }
    figure img { width: 100%; height: auto; border-radius: 10px; border: 1px solid #eee; }
    figcaption { font-size: 14px; color: #444; margin-top: 6px; }
    table { border-collapse: collapse; width: 100%; margin-top: 10px; font-size: 14px; }
    th, td { padding: 8px 10px; border-bottom: 1px solid #eee; text-align: left; }
    th { background: #f5f5f5; }
    .meta { color: #666; font-size: 13px; }
    @media (min-width: 900px) {
      .grid { grid-template-columns: 1fr 1fr; }
    }
  </style>
</head>
<body>
  <h1>O‘zbekiston: 12 viloyat ob-havo (7 kun)</h1>
  <p class="subtitle">Har bir viloyat bo‘yicha max/min harorat grafigi va jadval.</p>
  <div class="grid">
""")

for name, (lat, lon) in VILOYATLAR.items():
    try:
        df = fetch_weather(lat, lon)

        # saqlash
        safe_name = name.replace("‘", "'").replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        csv_path = os.path.join(CSV_DIR, f"{safe_name}.csv")
        img_path = os.path.join(IMG_DIR, f"{safe_name}.png")

        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        plot_weather(df, f"{name} — 7 kun (Max/Min)", img_path)

        # HTML blok
        table_html = df_to_html_table(df)
        img_rel = f"img/{safe_name}.png"

        html_parts.append(f"""
    <section class="card">
      <h2>{name}</h2>
      <div class="meta">Koordinata: {lat}, {lon}</div>
      <figure>
        <img src="{img_rel}" alt="{name} ob-havo grafigi">
        <figcaption>{name}: 7 kunlik maksimal va minimal harorat (°C)</figcaption>
      </figure>
      {table_html}
      <div class="meta">CSV: csv/{safe_name}.csv</div>
    </section>
""")
    except Exception as e:
        html_parts.append(f"""
    <section class="card">
      <h2>{name}</h2>
      <p style="color:#b00020;">Xatolik: {str(e)}</p>
    </section>
""")

html_parts.append("""
  </div>
</body>
</html>
""")

index_path = os.path.join(OUT_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print(f"✅ Tayyor! Ochish: {index_path}")
print("   Papka ichida: img/ (grafiklar) va csv/ (jadval ma'lumotlari)")