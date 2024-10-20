import getpass 
import mysql.connector 
from mysql.connector import Error

def create_database():
    connect = None
    try:
        user_name = input("Enter your msql username")
        password = getpass.getpass("Enter your password")
        connect = mysql.connector.connect(
            host = "localhost", 
            user = user_name, 
            password = password        
        )
        if connect.is_connected():
            cursor = connect.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print("There was an error connecting to your sql server!")
    except Error as e: 
        print(e)
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            print("The connection has been closed")
    
if __name__ == "__main__":
    create_database() 