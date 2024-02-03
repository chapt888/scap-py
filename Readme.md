# Inventory System Frontend Application

## Project Overview
- **Project Name** SCAP Frontend Application
- **Objective:** Develop a frontend application in Python to interact with an inventory system in a MySQL database.
- **Technology Stack:**
  - Frontend: `customtkinter` for UI
  - Backend: MySQL database
- **Structure:** The application will have a sidebar with a navigation menu and a main content area that changes based on the selected menu item.

## 1. Project Structure
Outline the directory structure and the naming conventions for the `.py` files.

### Directory Structure
- `/db` - for database connection and queries
- `/ui` - for UI components
- `/util` - for utility functions
- `/content_areas` - for different content areas

### Naming Conventions
- Files: `snake_case` (e.g., `database_connection.py`)
- Classes/Functions: `CamelCase` for classes and `snake_case` for functions

## 2. Database Connection
Details about setting up the module for database interactions.

### `db_connection.py`
- Function to connect to the MySQL database
- Function to close the database connection
- Query execution functions

## 3. Utilty Files
Utility Files needed for various functions in program.

### `vehicles_lookup.py`
- Will query the database for active vehicles and put the in an array for use in other pages dropdown menus.
  - Query: `select * from active_vehicles`

### `location_lookup.py`
- Will query the database for active locations and put the in an array for use in other pages dropdown menus.
  - Query: `select * from active_locations`

### `csv.py`
- Will handle converting mysql results to csv for download
- In the future may handle converting csv data for import to mysql table


## 4. UI Components
Design and development of the user interface.

### `main_window.py`
- Encases entire program
- Contains `sidebar.py` on the left side of window
- Conatins `main_content_area.py` on the right side of window

### `sidebar.py`
- Create a vertical navigation menu
- Buttons for different inventory sections

### `main_content_area.py`
- Logic to update the content based on the selected menu item

## 5. Content Area Management
Implementation of content area loading and display logic.

### Content Area Files (`/content_areas`)
- `parts.py`
- `vehicles.py`
- `locations.py`
- `reports.py`
- `operations.py`

## 6. Individual Content Area Files Components
Implementation of content area components loading and display logic.

### Content Area Components(`/content_areas`)
List of the components for each page that are to be build.

#### `parts.py`
- Frame with input field, submit button and treeview.
  - Input field to accept integer
  - Submit button will take integer and do a mysql query with following format: `select * from parts_car where 'sku' = 'parts_sku'`
    - The variable `parts_car` will be created by taking the integer and dropping the last 3 digits and appending 'car' to the beginning, ex: 1232 == car1.
    - The variable `parts_sku` will be the integer entered in the text field
  -Treeview will display the results from the mysql query
- Frame with Tabview with the following options:
  - Add Part
    - Will contain the following input and dropdown fields
      - Dropdown = car_select
      - Text box = item_name
      - Text box = mpn
      - Dropdown = location
      - Text box = size
      - Text box = weight
      - Dropdown = quality
      - Dropdown = status
      - Text box = sale_price
      - Text box = expense
      - Text box = profit
      - Submit button to insert the above inputs into a mysql table with "car_select" being the table name.
  - Update Part
    - Will contain the following input and dropdown fields
      - Dropdown = car_select
      - Text box = sku
      - Text box = item_name
      - Text box = mpn
      - Dropdown = location
      - Text box = size
      - Text box = weight
      - Dropdown = quality
      - Dropdown = status
      - Text box = sale_price
      - Text box = expense
      - Text box = profit
      - Submit button to update the above inputs into a mysql table with "car_select" being the table name and "sku" being the primary key.
  - Remove Part
    - Will contain a Input Field with a submit button
      - Text Box will accept and integer
      - Submit button will take integer and do a mysql query with following format: `delete from parts_car where 'sku' = 'parts_sku'`
        - The variable `parts_car` will be created by taking the integer and dropping the last 3 digits and appending 'car' to the beginning, ex: 1232 == car1.
        - The variable `parts_sku` will be the integer entered in the text field

#### `vehicles.py`
- Frame with Dropdown, submit button and treeview.
  - Dropdown will be populated by array from `vehicle_search.py`
  - Submit button will take option selected from dropdown and submit the following mysql query: `select * from 'Selected Option'`
  - Treeview will display results from query
- Frame with Tabview with the Following options:
  - Add Vehicle
    - Will include input field and Submit Button
      - Input Vehicle will accept string
      - Submit button will take the string inputted and do the following query: `Insert into active_vehicles ('Vehicle') values ('Input Field String')`
  - Update Vehicle
  WIP
  - Remove Vehicle
  WIP

#### `locations.py`
WIP

#### `reports.py`
WIP

#### `operations.py`
- QR Creator
  - Will include a Input Box and a Submit Button
    - Input Box will accept string
    - Submit button will create a static qr code from the string entered in the Input Box
- Download CSV
- Upload CSV



## 7. Modularity and Code Organization
Ensure code is organized, modular, and each `.py` file is self-contained.

### Best Practices
- Use classes and functions to encapsulate behavior
- Ensure clear interfaces between different modules
- Write reusable and well-documented code

## 8. Development Plan
A checklist or timeline to manage the development process.

### Step 1:
- [ ] Finalize the project structure
- [ ] Set up the database connection module

### Step 2:
- [ ] Develop the basic UI layout and build `main_window.py`
- [ ] Implement sidebar functionality and build `sidebar.py`

### Step 3:
- [ ] Develop `main_content_area.py`
- [ ] Develop content area for `parts.py`

### Step 4:
- [ ] Develop content area for `vehicles.py`

### Step 5:
- [ ] Develop content area for `locations.py`

### Step 6:
- [ ] Develop content area for `reports.py`

### Step 6:
- [ ] Develop content area for `operations.py`


## 9. Testing & Quality Assurance
Plan for testing the application to ensure it meets requirements and quality standards.

### Unit Tests
- Test database connection
- Test UI components in isolation

### Integration Tests
- Test the application flow from UI interaction to database updates

## 10. Deployment
Plan for deploying the application, including any required environment setup.

### Deployment Steps
- Environment setup
- Dependency installation
- Application launch instructions

