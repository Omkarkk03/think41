import pandas as pd
 
users= pd.read_csv('users.csv')
orders=pd.read_csv('orders.csv')
print("Users.csv sample:\n,",users.head(),"\n")
print("Orders.csv sample:\n,",orders.head(),"\n")