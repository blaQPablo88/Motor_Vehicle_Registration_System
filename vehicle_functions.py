from datetime import datetime

from pymongo import MongoClient

uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
database = client.get_database('dltc_db')
owner_collection = database.get_collection('owner')
vehicle_collection = database.get_collection('vehicle')

# from app import *

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select database and collection
db = client["dltc_db"]
collection = db["vehicle"]

# Query: Find all Toyota cars
query = {"vehicle_make": "honda"}
documents = collection.find(query, {"_id": 0, "vehicle_make": 1, "vehicle_model": 1, "year_of_manufacture": 1})

# Print results
for doc in documents:
    print(doc)


def vehicle_registration():
    """Handles vehicle registration."""
    first_name = input('enter first name: ')
    last_name = input('enter last name: ')
    id_number = input('enter id number: ')
    email = input('enter your email: ')
    phone_number = input('enter your phone number: ')
    physical_address = input('enter your physical address: ')

    # get recently registered license_plate to register this new one
    license_plate = input('enter license plate: ')

    vin_number = input('enter vin number:  ')
    vehicle_make = input('enter vehicle make:  ')
    vehicle_model = input('enter vehicle model:  ')
    year_of_manufacture = input('enter year of manufacture:  ')
    vehicle_color = input('enter vehicle color:  ')
    vehicle_type = input('enter vehicle type:  ')
    engine_number = input('enter engine number:  ')

    # get current date and time, `registered_at` should only update once

    try:
        query = {'license_plate': license_plate,
                 'vin_number': vin_number,
                 'vehicle_make': vehicle_make,
                 'vehicle_model': vehicle_model,
                 'year_of_manufacture': year_of_manufacture,
                 'vehicle_color': vehicle_color,
                 'vehicle_type': vehicle_type,
                 'engine_number': engine_number,
                 'registered_at': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                 'updated_at': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        }
        vehicle_results = vehicle_collection.insert_one(query)

        query = {'first_name': first_name,
                 'last_name': last_name,
                 'id_number': id_number,
                 'email': email,
                 'phone_number': phone_number,
                 'physical_address': physical_address,
                 'registered_at': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                 'updated_at': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        }
        owner_results = owner_collection.insert_one(query)

        if owner_results and vehicle_results is not None:
            print('Successfully registered')
        else:
            print('Registration unsuccessfully')
            return

    except Exception as e:
        raise Exception('Error', e)


def vehicle_change_ownership():
    """Handles change of ownership for a vehicle."""
    print("Vehicle ownership change process initiated.")

def vehicle_engine_change():
    """Handles vehicle engine change updates."""
    print("Vehicle engine change process initiated.")

def vehicle_deregister_vehicle():
    """Handles deregistration of a vehicle."""
    print("Vehicle deregistration process initiated.")

# Add more functions as needed...