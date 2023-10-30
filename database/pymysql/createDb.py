import dbconnection

cursor = dbconnection.db.cursor()

db_name = input("Enter a database name : ")
cursor.execute(f"create database {db_name}")