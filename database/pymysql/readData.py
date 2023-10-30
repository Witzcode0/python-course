import dbconnection

cursor = dbconnection.db.cursor()

table_name = input("Enter a table name: ")
cursor.execute(f"select * from {table_name}")

result = cursor.fetchall()

for record in result:
    print(list(record))