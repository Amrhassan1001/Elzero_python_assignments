#-----------------------------------------------------------------------
######################### Assignments 117 => 127 #######################
#-----------------------------------------------------------------------

# ######################### Assignment 1 #########################

import sqlite3

db = sqlite3.connect("app1.db")
cr = db.cursor()

cr.execute("create table if not exists data (a , b , c , d , e)")
cr.execute("insert into data(a , b , c , d , e) values(10 , 'Ten' , 10.00 , '$' , '[10]' )")

db.commit()
db.close()

# ######################### Assignment 2 #########################

import sqlite3

db = sqlite3.connect("Elzero.db")
cr = db.cursor()

cr.execute("create table if not exists Users \
(id integer Unique, name text Unique, date text Unique, email text Unique)")

db.commit()
db.close()

# ######################### Assignment 3 #########################

import sqlite3

db = sqlite3.connect("Elzero.db")
cr = db.cursor()

cr.execute("create table if not exists Users \
(id integer Unique, name text Unique, date text Unique, email text Unique)")

cr.execute("insert into Users(id , name , date , email ) values(1 , 'ahmed' , '10/1/2000' , 'ahmed@gmail.com' )")
cr.execute("insert into Users(id , name , date , email ) values(2 , 'sayad' , '22/2/1998' , 'sayad@gmail.com' )")
cr.execute("insert into Users(id , name , date , email ) values(3 , 'osama' , '5/4/2002'   , 'osama@gmail.com' )")
cr.execute("insert into Users(id , name , date , email ) values(4 , 'amr' , '1/1/2005' , 'amr@gmail.com' )")
cr.execute("insert into Users(id , name , date , email ) values(5 , 'mahmoud' , '10/11/2003' , 'mahmoud@gmail.com' )")

db.commit()
db.close()

# ######################### Assignment 4 #########################

import sqlite3

db = sqlite3.connect("Elzero.db")
cr = db.cursor()

cr.execute("select * from users")
a = cr.fetchall()
print(a[-1])

db.commit()
db.close()

# ######################### Assignment 5 #########################

import sqlite3

db = sqlite3.connect("Elzero.db")
cr = db.cursor()

cr.execute("select * from users")
a = cr.fetchall()

User_id = int(input("enter user id : ").strip())

def delete_user():
    cr.execute(f"delete from Users where id={User_id }")
    print("User deleted")

if User_id in range(len(a) + 1) :
    delete_user()
    cr.execute("select * from users")
    x = cr.fetchall()
    for i in range(len(x)) :
      print(f"ID => {x[i][0]}, Name => {x[i][1]}, Date Of Birth => {x[i][2]}, Email => {x[i][3]}")

else:
    print("user id is not found")

db.commit()
db.close()

# ############################# End ###############################
