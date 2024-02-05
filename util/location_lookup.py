# location_lookup.py

import sys
sys.path.insert(0, 'C:/Users/chapt/Desktop/scap-py')

from db.db_connection import DatabaseConnection

def get_locations():
    # Create an instance of DatabaseConnection
    db = DatabaseConnection()
    
    # Establish the database connection
    db.create_connection()

    # Define the query to get active vehicles
    query = "SELECT * FROM Locations"  # Assuming 'Locations' only has one column with the values you need

    # Execute the query
    result = db.execute_query(query)
    
    # Convert the result to a list
    # Adjust the index [0] if the structure is different
    location_list = [location[0] for location in result]
    
    # Close the database connection
    db.close_connection()

    return location_list
