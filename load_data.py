import pandas as pd
import sqlite3

users= pd.read_csv('users.csv')
orders=pd.read_csv('orders.csv')

conn = sqlite3.connect("ecommerce.db")


users.to_sql('users',conn,if_exists='append', index=False)
orders.to_sql('orders',conn,if_exists='append', index=False)

print("DATA inserted successfully.")
conn.close()