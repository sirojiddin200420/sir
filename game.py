import sqlite3

conn = sqlite3.connect("online_game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL UNIQUE,
    level INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (game_id) REFERENCES games(id)
)
""")

cursor.executemany("""
INSERT INTO players (nickname, level) VALUES (?, ?)
""", [
    ("Sirojiddin", 12),
    ("Ali", 8),
    ("Bek", 15),
    ("Jasur", 10),
    ("Lola", 9)
])

cursor.executemany("""
INSERT INTO games (game_name) VALUES (?)
""", [
    ("Minecraft",),
    ("PUBG",),
    ("Chess",)
])

cursor.executemany("""
INSERT INTO scores (player_id, game_id, score) VALUES (?, ?, ?)
""", [
    (1, 1, 250),
    (1, 2, 300),
    (2, 1, 180),
    (2, 3, 220),
    (3, 2, 500),
    (3, 3, 150),
    (4, 1, 270),
    (4, 2, 100),
    (5, 3, 350)
])

conn.commit()

print("Таблица players:")
for row in cursor.execute("SELECT * FROM players"):
    print(row)

print("\nТаблица games:")
for row in cursor.execute("SELECT * FROM games"):
    print(row)

print("\nТаблица scores:")
for row in cursor.execute("SELECT * FROM scores"):
    print(row)

print("\nТОП-3 игроков по очкам:")
for row in cursor.execute("""
SELECT players.nickname, SUM(scores.score) AS total_score
FROM scores
JOIN players ON players.id = scores.player_id
GROUP BY players.id, players.nickname
ORDER BY total_score DESC
LIMIT 3
"""):
    print(row)

conn.close()