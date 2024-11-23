# vehicle_collection = database.get_collection('vehicles')

# Import all functions
from vehicle_functions import (
    vehicle_registration,
    vehicle_change_ownership,
    vehicle_engine_change,
    vehicle_deregister_vehicle
)

def main_menu():
    print("\nSelect an option:")
    print("1 -> Vehicle Registration")
    print("2 -> Change Ownership")
    print("3 -> Engine Change")
    print("4 -> Deregister Vehicle")

    # Get user input
    choice = int(input("Enter your choice: "))

    # Map input to functions
    options = {
        1: vehicle_registration,
        2: vehicle_change_ownership,
        3: vehicle_engine_change,
        4: vehicle_deregister_vehicle,
    }

    # Execute the chosen function
    func = options.get(choice)
    if func:
        func()
    else:
        print("Invalid choice. Please try again.")

# Run the menu
main_menu()
