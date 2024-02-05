
# SCAP Inventory Database Schema

## Tables and Fields

### 1. Vehicles
- **VehicleID** (INT, Primary Key): A unique identifier for each vehicle.
- **Year** (YEAR): The year the vehicle was manufactured.
- **Make** (VARCHAR): The manufacturer of the vehicle.
- **Model** (VARCHAR): The model of the vehicle.
- **Trim** (VARCHAR): The specific version or configuration of the model.
- **VIN** (VARCHAR): VIN number of vehicle

### 2. Parts
- **PartID** (INT, Primary Key): A unique identifier for each part.
- **VehicleID** (INT, Foreign Key): The identifier of the vehicle from which the part was taken.
- **Name** (VARCHAR): The name or description of the part.
- **PartNumber** (VARCHAR): An identifier or number given to the part, if applicable.
- **LocationID** (INT, Foreign Key): The identifier of the location where the part is stored.
- **Size** (VARCHAR): The Dimensions of the part.
- **Weight** (VARCHAR): The Weight of the part.
- **Quality** (VARCHAR): The Quality of the part.
- **Status** (VARCHAR): The current Status of the part.
- **PartSequence** (INT): Counter for PartID Trigger

### 3. Locations
- **LocationID** (INT, Primary Key): A unique identifier for each location.
- **Description** (TEXT): A description of the location.

### 4. VehicleCosts
- **CostID** (INT, Primary Key): A unique identifier for each cost entry.
- **VehicleID** (INT, Foreign Key): The identifier of the vehicle.
- **CostType** (VARCHAR): A description of the cost (e.g., Purchase, Transportation).
- **Amount** (DECIMAL): The monetary value of the cost.
- **DateIncurred** (DATE): The date the cost was incurred.

### 5. PartSales
- **SaleID** (INT, Primary Key): A unique identifier for each sale.
- **PartID** (INT, Foreign Key): The identifier of the part that was sold.
- **SalePrice** (DECIMAL): The selling price of the part.
- **SaleDate** (DATE): The date the part was sold.

### 6. PartCosts
- **CostID** (INT, Primary Key): A unique identifier for each cost entry.
- **PartID** (INT, Foreign Key): The identifier of the part.
- **CostType** (VARCHAR): A description of the cost (e.g., Cleaning, Refurbishing).
- **Amount** (DECIMAL): The monetary value of the cost.
- **DateIncurred** (DATE): The date the cost was incurred.

### 7. ActiveVehicles
- **ActiveVehicle** (VARCHAR): Contains Vehicles Currently Active

## Relationships
- **Vehicles to Parts**: One-to-Many (One vehicle can have many parts, but each part comes from one specific vehicle).
- **Parts to Locations**: Many-to-One (Many parts can be stored in one location, but each part is stored in one specific location).
- **Parts to PartSales**: One-to-One (Each part can be sold once).
- **Parts to PartCosts**: One-to-Many (Each part can have multiple costs associated with it).
- **Vehicles to VehicleCosts**: One-to-Many (Each vehicle can have multiple costs associated with it).
