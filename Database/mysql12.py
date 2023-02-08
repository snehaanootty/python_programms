import pymysql
db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
con=db.cursor()
sqlquery="insert into t1 values(%s,%s,%s)"
val=(22,'anju',89)
con.execute(sqlquery,val)
db.commit()
print("inserted")


import pymysql
id=int(input("enter the id:"))
na=input("enter the name:")
age=int(input("enter the age:"))
db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
con=db.cursor()
sql="insert into t1 values(%s,%s,%s)"
val=(id,na,age)
con.execute(sql,val)
db.commit()
print("inserted")


import pymysql
id=int(input("enter the id:"))
db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
mycursor=db.cursor()
sql="delete from t1 where id='%d'"%(id)
mycursor.execute(sql)
db.commit()
print("deleted")


import pymysql
y=input("do you want to upadte:")
if y=="yes":
    db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
    id=int(input("enter the id:"))
    na=input("enter the name:")
    age=int(input("enter the age:"))
    c=db.cursor()
    sql="update t1 set name='%s',age='%s' where id='%d' "%(na,age,id)
    c.execute(sql)
    db.commit()
    print("updated")
elif y=="no":
    print("exit")
else:
    print("invalid")


import pymysql
id=int(input("enter the id:"))
db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
con=db.cursor()
sql='select * from t1 where id=%d' %id
con.execute(sql)
i=con.fetchone()
id=i[0]
na=i[1]
age=i[2]
print(f'id= {i[0]}, name={na}, age={age}')


import pymysql
db=pymysql.connect(host="localhost",user="root",password="@mayA!/2002",database="nov_test")
con=db.cursor()
sql="select * from t1 "
con.execute(sql)
data=con.fetchall()
for i in data:
    id= i[0]
    na= i[1]
    age= i[2]
    print(f'id= {i[0]}, name={na}, age={age}')