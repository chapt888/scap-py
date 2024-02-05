# db_connection.py

import sys
sys.path.insert(0, 'C:/Users/chapt/Desktop/scap-py')

import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        # Database connection parameters
        self.host = '192.168.69.2'
        self.database = 'scap_inv_test'
        self.user = 'root'
        self.password = 'Modex88$'
        self.conn = None

    def create_connection(self):
        """Create a database connection."""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.conn.is_connected():
                print("MySQL database connection is successful.")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.conn.is_connected():
            self.conn.close()
            print("MySQL connection is closed.")

    def execute_query(self, query):
        """Execute a given SQL query."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
