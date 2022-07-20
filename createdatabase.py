import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='Saurabh@23',
              database='college')

cursor= con.cursor()

while True:

    name=input("enter the name")
    age= int(input("enter the age"))
    marks=int(input("enter the marks"))

    query="insert into student values('{}',{},{})".format(name,age,marks)
    cursor.execute(query)
    con.commit()

    print("data created successfully")

    choice=input("1.enter more data\n2.exit")
    if choice=="2":
        break



