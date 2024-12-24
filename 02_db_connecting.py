# connecting to tje db 
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
try:
    if mydb.is_connected():
        print("connected")
except:
    # check the error and print back to the users 
    print(mydb.errors)
    print("not connected")
finally:
    print("database basic handeling is done !!")
