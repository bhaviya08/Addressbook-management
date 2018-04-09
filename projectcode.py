
import sqlite3
#DATABSE CONNECTION (Refer to file projectdb)
conn=sqlite3.connect("ADDRESSBOOK.db")
print("DATABASE CONNECTION SUCSSESS")
#conn.execute("DROP table IF EXISTS address ")
#conn.execute("""CREATE table address
#           (NAME varchar(20) not null,
#             NUMBER int(15) not null,
#             EMAIL VARCHAR(40) not null,
#             notes char(100) not NULL
#             );""")

#WELCOME
print("WELCOME TO ADDRESS BOOK")
print("\n        MENU \n 1. ADD CONTACT \n 2. ALL CONTACTS \n 3. DELETE CONTACT \n 4. UPDATE CONTACT \n 5. SEARCH CONTACT \n")

global a,b,c,d
#FUNCTION DEFINITIONS
def INSERT(a,b,c,d):
    a = input("ENTER NAME :")
    b = int(input("ENTER NUMBER :"))
    c = input("ENTER EMAIL :")
    d = input("ENTER NOTES :")
    conn.execute("INSERT INTO address(NAME,NUMBER,EMAIL,notes) VALUES(?,?,?,?)",(a,b,c,d))
    conn.commit()
    print("DATA INSERTED SUCCESSFULLY")



def ALLCONTACTS():
    p = conn.execute("SELECT NAME,NUMBER,EMAIL,notes FROM address ORDER BY NAME ASC ");
    for i in p:
        print("NAME: ", i[0])
        print("NUMBER: ", i[1])
        print("EMAIL: ", i[2])
        print("NOTES: ", i[3])
        print("\n")
        z = conn.execute('SELECT count(NAME) FROM address');
    print("TOTAL CONTACTS :",z.fetchone())


global d1
def DELETE(d1):
    c1=conn.cursor()

    d1 = input("ENTER CONTACT NAME YOU WANT TO DELETE :")
    e = list(c1.execute("Select * from address where NAME=?", (d1,)))
    if len(e)==0:
        print("Doesn't exist")
    else:
        conn.execute('DELETE FROM address WHERE NAME=?',(d1,))
        print("CONTACT DELETED SUCCSESSFULY")
        conn.commit()

def SEARCH(s1):
    c1=conn.cursor()
    s1=input("ENTER NAME TO SEARCH :")
    p= list(c1.execute("Select * from address where NAME=?", (s1,)))
    if len(p) == 0:
        print("CONTACT Doesn't exist")
    else:
        s2=conn.execute('SELECT NUMBER,EMAIL,notes FROM address where NAME=?',(s1,))
        for r in s2:
            print("NUMBER:",r[0])
            print("EMAIL:", r[1])
            print("NOTES:",r[2])
            print("\n")
    conn.commit()

global u1,u2,u3,u4
def UPDATE(u1,u2,u3,u4,):
    c1 = conn.cursor()
    u1=input("ENTER CONTACT NAME TO UPDATE :")
    t= list(c1.execute("Select * from address where NAME=?", (u1,)))
    if len(t) == 0:
        print("CONTACT Doesn't exist")
    else:
        u2 = input("ENTER NEW NUMBER  :")
        u3 = input("ENTER NEW EMAIL  :")
        u4 = input("ENTER NOTE  :")
        conn.execute('UPDATE address set NUMBER=? ,EMAIL=? ,notes=? WHERE NAME=?',(u2,u3,u4,u1))
        conn.commit()
        print("CONTACT UPDATED")




#MENU PROG
ans=True
while ans:
    ans=input("ENTER YOUR CHOICE: ")
    if ans=="1":
        INSERT('a','b','c','d')
        break
    elif ans=="2":
        ALLCONTACTS()
        break
    elif ans=="3":
        DELETE('d1')
        break
    elif ans=="4":
        UPDATE('u1','u2','u3','u4')
        break
    elif ans=="5":
        SEARCH('s1')
        break
    else:
        print("\n WRONG INPUT, ENTER AGAIN \n ")




