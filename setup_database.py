import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    created_at TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    created_at TEXT,
    returned_at TEXT,
    shipped_at TEXT,
    delivered_at TEXT,
    num_of_item INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")


conn.commit()
conn.close()

print("Tables created successfully.")
