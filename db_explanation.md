## Database Explanation

### 1. Overall
This database is for Inventory for a company that "parts out" vehicles. This means they recieve a vehicle and remove the parts from said vehicle and store them in locations until sold. The parts from the vehicle are the product. The vehicles are the raw good that the parts come from and locations are where the product is stored until sold.
There are 3 main objects that are tracked in this datatbase.
- Vehicles
- Parts
- Locations

### 2. Vehicles
There will be multiple vehicles tracked and all vehicle information will be stored indefinitly. The information needed tracked for each vehicle is as follows.
- Vehicle Information for each vehicle
    - The information that applies only to this specific vehicle that includes:
        - ID, Unique ID for each specific vehicle
        - Year, The year this vehicle was manufactured
        - Make, The original company that manufactured vehicle
        - Model, The model name assigned by OEM
        - Trim, Trim level of vehicle
        - VIN, Serial number assigned by OEM
        - Purchase_Price, amount company purchase vehicle for
        - Expenses, Total of all Expenses Accured by Vehicle
        - Sale_Price, Total of all parts sell price
        - Profit, Sale_Price - Expenses = Profit        
- Parts that are pulled from each vehicle and their respective information explained in section 3
- The Active Vehicles being worked on.
    - This information will be used to populate dropdown boxes in a python program so that new parts can only be entered into active vehicles
    - Once a vehicle is recieved to be worked on by company it will be added to this list
    - Once company has finished with this vehicle and all parts have been sold or scrapped, the vehicle will be taken off this list

### 3. Parts
There will be up to 999 parts per vehicle and the following info for each is as follows:
- Parts Information
    - SKU, Unique ID for each part that is the `Vehicle ID` with with a 3 digit number auto assign and append on the end of the `Vehicle ID` starting at 001.
        - EX: The first part for Vehicle that has the ID of 1 will have the SKU: 1001
    - Item Name, The Name of the part
    - MPN, OEM part number assigned by the original manufacturer at the factory
    - Location, The location the part is stored it after removal from the Vehicle while it waits to be sold. Explained more in section 4.
    - Size, The dimensional size of the part
    - Weight, The weight of the part
    - Quality, The Quality of the part. One of the following options:
        - Core, The part is only good for scrap
        - Rough, The part is cosmetically damage which may need repaired or affect sale price
        - Good, The part is in good condition
    - Status, The Status of the part. One of the following options:
        - Scrap, The part is not good to be sold
        - Unlisted, Part is not yet listed for sale
        - Listed, Part is listed for sale
        - Sold, Part has sold

### 4. Locations
Each Location is a place to store parts until they are sold. These will need to be able to be searched by location and see all parts in that locations even if those parts belong to multiple vehicles. Parts should be able to be added and taken out of Locations easily.


