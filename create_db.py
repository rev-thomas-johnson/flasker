import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Password123",
	)

my_cursor = mydb.cursor()

# Uncomment nextline to run
# my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)