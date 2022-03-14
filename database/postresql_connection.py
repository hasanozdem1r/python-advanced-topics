# pip install psycopg2
import psycopg2

# Connection string used to connect with the server
connection = psycopg2.connect(
    host="localhost", database="database_name", user="user_name", password="password"
)

cursor = connection.cursor()
cursor.execute("SELECT version()")
version = cursor.fetchone()
print("Database Version : {}".format(version))
