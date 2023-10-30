import dbconnection

cursor = dbconnection.db.cursor()
table_name = input("Enter a table name : ")

flag = True
empty = ""
while flag:
    yesNo = input("you want to add new field? y/n : ")
    if yesNo.lower() == 'y':
        field = input("Enter a field with datatype : ")
        empty += f" {field} "
    else:
        flag = False

sql = f'create table {table_name}({empty})'
print(sql)
cursor.execute(sql)