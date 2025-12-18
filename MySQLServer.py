

import mysql.connector
from mysql.connector import Error

try:
    # CONNECT TO MYSQL SERVER
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password ="Debramugwe@1",
        

        
    )

    mycursor = mydb.cursor()

    # CREATE DATABASE
    mycursor.execute(
        "CREATE DATABASE IF NOT EXISTS alx_book_store"
    )

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # CLOSE CONNECTIONS
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Database connection closed.")
