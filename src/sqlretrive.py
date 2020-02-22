import mysql.connector

conn = mysql.connector.connect(host = 'localhost',username='root',password='1234', database = 'face')

print(conn)

my_cursor = conn.cursor()
query2 = "SELECT * FROM student"
my_cursor.execute(query2)

for row in my_cursor:
    print(row)

    
conn.commit()
conn.close()
