import mysql.connector

mydb = mysql.connector.connect(
	host="localhost:8080",
	user="block011",
	passwd="test"
 )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")