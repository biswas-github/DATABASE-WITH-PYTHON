import mysql.connector

# Establishing connection to the MySQL server
database_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"  # Specify the database name
)

cursor = database_connection.cursor()

# SQL query to insert a record into the student table
SQL = "INSERT INTO student (name, grade) VALUES (%s, %s)"
values = ("Bibas Banstola", 4)  # Passing values as a tuple

# Executing the query with the provided values
cursor.execute(SQL, values)

# Print the number of rows affected
print("..........No of affected rows..........")
print(cursor.rowcount, "row(s) have been changed/inserted")

# Commit the transaction to save the changes
database_connection.commit()

# Closing the database connection
database_connection.close()
