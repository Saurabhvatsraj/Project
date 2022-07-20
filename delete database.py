import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='Saurabh@23',
              database='college')

cursor=con.cursor()
marks=int(input("enter the marks"))

query="delete from student where marks ={}".format(marks)

cursor.execute(query)
con.commit()

print("delete database successfully")