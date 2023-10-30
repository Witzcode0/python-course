import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="instagram"
)

if db:
    print("Connection successfully done.")