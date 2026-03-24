import sqlite3

# -------- 1. Подключение к базе --------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# -------- 2. Создание таблицы --------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    student_group TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
)
""")

# -------- 3. Добавление данных --------
students = [
    (1, 'Иван Петров', 19, 'IT-21', 'ivan.petrov@mail.com', '+998901112233'),
    (2, 'Анна Сидорова', 21, 'IT-21', 'anna.sidorova@mail.com', '+998901234567'),
    (3, 'Дмитрий Карпов', 22, 'CS-22', 'dmitry.karpov@mail.com', '+998907654321'),
    (4, 'Мария Иванова', 20, 'IT-20', 'maria.ivanova@mail.com', '+998909876543'),
    (5, 'Алексей Смирнов', 23, 'IT-21', 'alexey.smirnov@mail.com', '+998903334455')
]

cursor.executemany("INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?, ?)", students)

conn.commit()

# -------- 4. Запросы --------

# Все студенты
print("\nВсе студенты:")
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# Старше 20 лет
print("\nСтуденты старше 20:")
cursor.execute("SELECT * FROM Students WHERE age > 20")
for row in cursor.fetchall():
    print(row)

# Группа IT-21
print("\nСтуденты группы IT-21:")
cursor.execute("SELECT * FROM Students WHERE student_group = 'IT-21'")
for row in cursor.fetchall():
    print(row)

# -------- 5. Аналитика --------

# Общее количество
cursor.execute("SELECT COUNT(*) FROM Students")
print("\nВсего студентов:", cursor.fetchone()[0])

# В группе IT-21
cursor.execute("SELECT COUNT(*) FROM Students WHERE student_group = 'IT-21'")
print("В группе IT-21:", cursor.fetchone()[0])

# Средний возраст
cursor.execute("SELECT AVG(age) FROM Students")
print("Средний возраст:", cursor.fetchone()[0])

# -------- 6. Закрытие --------
conn.close()