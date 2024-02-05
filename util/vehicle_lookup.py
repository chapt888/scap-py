# vehicles_lookup.py

import sys
sys.path.insert(0, 'C:/Users/chapt/Desktop/scap-py')

from db.db_connection import DatabaseConnection

def get_active_vehicles():
    # Create an instance of DatabaseConnection
    db = DatabaseConnection()
    
    # Establish the database connection
    db.create_connection()

    # Define the query to get active vehicles
    query = "SELECT * FROM ActiveVehicles"  # Assuming 'ActiveVehicles' only has one column with the values you need

    # Execute the query
    result = db.execute_query(query)
    
    # Convert the result to a list (assuming the column name is 'VehicleName' or similar)
    # Adjust the index [0] if the structure is different
    vehicles_list = [vehicle[0] for vehicle in result]
    
    # Close the database connection
    db.close_connection()

    return vehicles_list
