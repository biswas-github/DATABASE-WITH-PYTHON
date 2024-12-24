import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
print(mydb)
#creating the cursor
mycursor=mydb.cursor()
# ?execute the cursor for adding data in the db
mycursor.execute("SELECT * FROM testdb.student")
# printing the data in the my cursor 
for x in mycursor:
    print(x)
mycursor.execute("SHOW DATABASES")
print("the databases are as :-")
for x in mycursor:
    print(x)
# now program for the showing the tables inside the db testdb
mycursor.execute("USE testdb")
mycursor.execute("SHOW TABLES")
print(" tables are \n")
for x in mycursor:
    print(x)
