# test_location_lookup.py
import sys
sys.path.insert(0, 'C:/Users/chapt/Desktop/scap-py')

# test_location_lookup.py

from util.location_lookup import get_locations

def test_get_locations():
    location_list = get_locations()
    print("Active Locations:")
    for name in location_list:
        print(name)

if __name__ == "__main__":
    test_get_locations()

