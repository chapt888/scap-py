# test_vehicle_lookup.py
import sys
sys.path.insert(0, 'C:/Users/chapt/Desktop/scap-py')

# test_vehicle_lookup.py

from util.vehicle_lookup import get_active_vehicles

def test_get_active_vehicles():
    vehicle_names = get_active_vehicles()
    print("Active Vehicle Names:")
    for name in vehicle_names:
        print(name)

if __name__ == "__main__":
    test_get_active_vehicles()

