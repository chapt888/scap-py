## Database Schema

This section outlines the structure of the database used by the SCAP Frontend Application. Each table is designed to hold specific types of information critical to the inventory system's functionality.

### Table Descriptions

#### 1. `car1`
- **Purpose:** Hold the parts and information for each part that came from car1.
- **Fields:**
  - `sku`: The Stock Number for each particular part. Primary key and unique identifier for the table. Auto incremented when item added to table
  - `item_name`: Name for the Part
  - `mpn`: Part number given to the part by the manufacturer
  - `location`: Location part is currently stored in
  - `size`: Dimensions of the part
  - `weight`: Weight of the part
  - `quality`: Quality status for the parts
  - `status`: Wether the part has been listed for sale or not or sold
  - `sale_price`: Price part sold for
  - `expense`: Expenses related to part
  - `profit`: sale_price - expense
- **Relationships:** In the database testdb. location options are from the `active_locations` table and the table name is from the `active_vehicles` table. There is one of these table for each line of `active_vehicles`.

#### 2. `active_locations`
- **Purpose:** Stores all the active storage locations for parts.
- **Fields:**
  - `Location`: The name of the storage location.
- **Relationships:** Used to populate storage location options for program and car tables.

#### 3. `active_vehicles`
- **Purpose:** The currently active vehicles we have parts for.
- **Fields:**
  - `Vehicle`: Name of active vehicle
- **Relationships:** Populates the dropdowns for the program.

... (and so on for each table in your database)

### Relationships Diagram
(Optional) Include a diagram or an image that visually represents the relationships between the tables. This can help in understanding the overall structure and how different tables interact with each other.

![Database Schema Diagram](path_to_your_image.png)

### Additional Notes
- Any specific conventions followed (e.g., naming conventions, primary key and foreign key constraints).
- Any triggers, stored procedures, or specific database functionalities used.
