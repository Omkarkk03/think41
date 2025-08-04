import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor= conn.cursor()

print("first 5 users:")
for row in cursor.execute("SELECT * FROM users LIMIT 5"):
    print(row)
print("\nfirst 5 orders:")
for row in cursor.execute("SELECT * FROM orders LIMIT 5"):
    print(row)
conn.close()
