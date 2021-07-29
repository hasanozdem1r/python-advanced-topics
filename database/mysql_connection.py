import mysql.connector

#Connection string used to connect with the server
db_connection = mysql.connector.connect(
  host="localhost",
  user="user_name",
  password="password"
)
print(db_connection)
if db_connection:
  print("Connected")