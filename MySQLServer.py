import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (NOT to a specific DB yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password2025'  # replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database (if not exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"❌ Failed to connect or create database: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
