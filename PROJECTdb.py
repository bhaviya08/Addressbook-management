import sqlite3
conn=sqlite3.connect("ADDRESSBOOK.db")
print("DATABASE CONNECTION SUCSSESS")
#conn.execute("DROP table IF EXISTS address ")
#conn.execute("""CREATE table address
#           (NAME varchar(20) not null,
#             NUMBER int(15) not null,
#             EMAIL VARCHAR(40) not null,
#             notes char(100) not NULL
#             );""")
#print("TABLE CREATED SUCCSESSFULLY")





