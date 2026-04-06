import sqlite3

conn = sqlite3.connect("ticket_system.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Payments")
cursor.execute("DROP TABLE IF EXISTS Tickets")
cursor.execute("DROP TABLE IF EXISTS Events")
cursor.execute("DROP TABLE IF EXISTS Users")

cursor.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL,
    price REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Tickets (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    purchase_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (event_id) REFERENCES Events(id)
)
""")

cursor.execute("""
CREATE TABLE Payments (
    id INTEGER PRIMARY KEY,
    ticket_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES Tickets(id)
)
""")

users = [
    (1, 'Ali Valiyev', 'ali@mail.com', '+998901111111'),
    (2, 'Sardor Karimov', 'sardor@mail.com', '+998902222222'),
    (3, 'Malika Ruzieva', 'malika@mail.com', '+998903333333'),
    (4, 'Javohir Tursunov', 'javohir@mail.com', '+998904444444'),
    (5, 'Nodira Ergasheva', 'nodira@mail.com', '+998905555555')
]

events = [
    (1, 'Rock Concert', 'Tashkent', '2026-04-10', 120.0),
    (2, 'Cinema Premiere', 'Samarkand', '2026-04-15', 80.0),
    (3, 'IT Forum', 'Bukhara', '2026-05-01', 150.0),
    (4, 'Comedy Show', 'Tashkent', '2026-04-20', 95.0),
    (5, 'Jazz Festival', 'Khiva', '2026-05-10', 130.0),
    (6, 'Art Exhibition', 'Nukus', '2026-05-20', 70.0)
]

tickets = [
    (1, 1, 1, '2026-03-20'),
    (2, 1, 3, '2026-03-21'),
    (3, 2, 2, '2026-03-22'),
    (4, 2, 1, '2026-03-23'),
    (5, 3, 4, '2026-03-24'),
    (6, 3, 5, '2026-03-25'),
    (7, 4, 3, '2026-03-26'),
    (8, 4, 1, '2026-03-27'),
    (9, 5, 2, '2026-03-28'),
    (10, 5, 5, '2026-03-29')
]

payments = [
    (1, 1, 120.0, 'Paid'),
    (2, 2, 150.0, 'Paid'),
    (3, 3, 80.0, 'Paid'),
    (4, 4, 120.0, 'Pending'),
    (5, 5, 95.0, 'Paid'),
    (6, 6, 130.0, 'Paid'),
    (7, 7, 150.0, 'Pending'),
    (8, 8, 120.0, 'Paid'),
    (9, 9, 80.0, 'Paid'),
    (10, 10, 130.0, 'Paid')
]

cursor.executemany("INSERT INTO Users VALUES (?, ?, ?, ?)", users)
cursor.executemany("INSERT INTO Events VALUES (?, ?, ?, ?, ?)", events)
cursor.executemany("INSERT INTO Tickets VALUES (?, ?, ?, ?)", tickets)
cursor.executemany("INSERT INTO Payments VALUES (?, ?, ?, ?)", payments)

conn.commit()

def show_results(title, query, params=()):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("Natija topilmadi")

show_results(
    "1. Barcha foydalanuvchilar",
    "SELECT * FROM Users"
)

show_results(
    "2. Narxi 100$ dan qimmat bo'lgan tadbirlar",
    "SELECT * FROM Events WHERE price > 100"
)

show_results(
    "3. Aniq bir foydalanuvchining biletlari (user_id = 1)",
    "SELECT * FROM Tickets WHERE user_id = ?",
    (1,)
)

show_results(
    "4. Foydalanuvchilar va ularning biletlari (JOIN)",
    """
    SELECT Users.name, Events.title, Tickets.purchase_date
    FROM Tickets
    JOIN Users ON Tickets.user_id = Users.id
    JOIN Events ON Tickets.event_id = Events.id
    """
)

show_results(
    "5. Tadbirlar va sotilgan biletlar soni",
    """
    SELECT Events.title, COUNT(Tickets.id) AS tickets_sold
    FROM Events
    LEFT JOIN Tickets ON Events.id = Tickets.event_id
    GROUP BY Events.id, Events.title
    """
)

show_results(
    "6. Har bir tadbir bo'yicha umumiy to'lov summasi",
    """
    SELECT Events.title, IFNULL(SUM(Payments.amount), 0) AS total_paid
    FROM Events
    LEFT JOIN Tickets ON Events.id = Tickets.event_id
    LEFT JOIN Payments ON Tickets.id = Payments.ticket_id AND Payments.status = 'Paid'
    GROUP BY Events.id, Events.title
    """
)

show_results(
    "7. Eng ko'p bilet sotib olgan foydalanuvchi",
    """
    SELECT Users.name, COUNT(Tickets.id) AS total_tickets
    FROM Users
    JOIN Tickets ON Users.id = Tickets.user_id
    GROUP BY Users.id, Users.name
    ORDER BY total_tickets DESC
    LIMIT 1
    """
)

show_results(
    "8. Faqat to'langan biletlar",
    """
    SELECT Tickets.id, Users.name, Events.title, Payments.amount, Payments.status
    FROM Tickets
    JOIN Users ON Tickets.user_id = Users.id
    JOIN Events ON Tickets.event_id = Events.id
    JOIN Payments ON Tickets.id = Payments.ticket_id
    WHERE Payments.status = 'Paid'
    """
)

show_results(
    "9. Xarid qilinmagan tadbirlar",
    """
    SELECT Events.*
    FROM Events
    LEFT JOIN Tickets ON Events.id = Tickets.event_id
    WHERE Tickets.id IS NULL
    """
)

show_results(
    "10. Tadbirlarni sana bo'yicha saralash",
    "SELECT * FROM Events ORDER BY date ASC"
)

conn.close()