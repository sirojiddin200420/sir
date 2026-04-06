import sqlite3
# 1. Подключение к базе данных
conn = sqlite3.connect("it_projects.db")
cursor = conn.cursor()
# 2. Включение внешних ключей
cursor.execute("PRAGMA foreign_keys = ON;")
# 3. Удаление таблиц
cursor.execute("DROP TABLE IF EXISTS comments")
cursor.execute("DROP TABLE IF EXISTS tasks")
cursor.execute("DROP TABLE IF EXISTS sprints")
cursor.execute("DROP TABLE IF EXISTS projects")
cursor.execute("DROP TABLE IF EXISTS developers")
# 4. Создание таблиц
cursor.execute("""
CREATE TABLE developers (
    developer_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    level TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    deadline TEXT NOT NULL,
    budget REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE sprints (
    sprint_id INTEGER PRIMARY KEY,
    project_id INTEGER NOT NULL,
    sprint_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
""")

cursor.execute("""
CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY,
    project_id INTEGER NOT NULL,
    sprint_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    task_title TEXT NOT NULL,
    status TEXT NOT NULL,
    priority TEXT NOT NULL,
    estimated_hours INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (sprint_id) REFERENCES sprints(sprint_id),
    FOREIGN KEY (developer_id) REFERENCES developers(developer_id)
)
""")

cursor.execute("""
CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY,
    task_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    comment_text TEXT NOT NULL,
    comment_date TEXT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (developer_id) REFERENCES developers(developer_id)
)
""")

# 5. Данные
developers_data = [
    (1, 'Aziza Murodova', 'Backend', 'Middle'),
    (2, 'Bekzod Alimuhamedov', 'Frontend', 'Junior'),
    (3, 'Kamron Yusupov', 'Data Engineer', 'Senior'),
    (4, 'Nilufar Sobirova', 'QA Engineer', 'Middle')
]

projects_data = [
    (1, 'SmartEdu Platform', '2025-01-10', '2025-06-30', 120000000),
    (2, 'MedNavigator App', '2025-02-01', '2025-08-15', 95000000)
]

sprints_data = [
    (1, 1, 'Sprint 1', '2025-01-10', '2025-01-24'),
    (2, 1, 'Sprint 2', '2025-01-25', '2025-02-08'),
    (3, 2, 'Sprint 1', '2025-02-01', '2025-02-15')
]

tasks_data = [
    (1, 1, 1, 1, 'Develop user authentication API', 'Done', 'High', 20),
    (2, 1, 1, 2, 'Create login page UI', 'Done', 'Medium', 16),
    (3, 1, 2, 4, 'Test authorization module', 'In Progress', 'High', 12),
    (4, 2, 3, 3, 'Design patient location data pipeline', 'In Progress', 'High', 30),
    (5, 2, 3, 1, 'Build appointment scheduling service', 'To Do', 'High', 24)
]

comments_data = [
    (1, 1, 1, 'API endpoints implemented and tested', '2025-01-20'),
    (2, 2, 2, 'UI ready for review', '2025-01-22'),
    (3, 3, 4, 'Need additional edge-case testing', '2025-02-02'),
    (4, 4, 3, 'Pipeline schema drafted', '2025-02-10'),
    (5, 5, 1, 'Waiting for business logic clarification', '2025-02-12')
]

cursor.executemany("INSERT INTO developers VALUES (?, ?, ?, ?)", developers_data)
cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", projects_data)
cursor.executemany("INSERT INTO sprints VALUES (?, ?, ?, ?, ?)", sprints_data)
cursor.executemany("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tasks_data)
cursor.executemany("INSERT INTO comments VALUES (?, ?, ?, ?, ?)", comments_data)

conn.commit()

# 6. Практические задания

print("\nЗадание 1. Все задачи вместе с именем разработчика и названием проекта")
cursor.execute("""
SELECT t.task_title, d.full_name, p.project_name, t.status, t.priority
FROM tasks t
JOIN developers d ON t.developer_id = d.developer_id
JOIN projects p ON t.project_id = p.project_id
""")
for row in cursor.fetchall():
    print(row)