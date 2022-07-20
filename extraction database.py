import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='Saurabh@23',
              database='college')

cursor=con.cursor()

query="select * from students"

cursor.execute (query)

data= cursor.fetchone()
con.commit()

