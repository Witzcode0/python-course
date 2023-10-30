import dbconnection

cursor = dbconnection.db.cursor()

flag = True
while flag:
    yesNo = input("you want to add new record? y/n : ")
    if yesNo.lower() == 'y':
        fname = input("Enter a fname : ")
        lname = input("Enter a lname : ")
        age = input("Enter a age : ")
        cursor.execute(f"insert into users(fname, lname, age)values('{fname}', '{lname}', {age})")
    else:
        flag = False

dbconnection.db.commit()