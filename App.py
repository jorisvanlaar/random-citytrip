"""Joris van laar - Python (PTH) - 20-01-2020"""
import pickle
from pyfiglet import figlet_format
from termcolor import colored
from random import choice
from Reservation import Reservation
from Customer import Customer
from Destination import Destination
from Bicycle import Bicycle
from Car import Car
from Boat import Boat
from Train import Train
from Airplane import Airplane
from Hovercraft import Hovercraft


def logo():
    ascii_logo = figlet_format("Random CityTrip")
    colored_logo = colored(ascii_logo, color='yellow')
    print(colored_logo)


def greeting():
    print("Welcome to Random CityTrip!\n"
          "Up for some adventure?\n"
          "We'll randomly select a city for you, and you decide how to get there from Amsterdam.")


def menu():
    while True:
        print("\nMENU")
        print("[1] Book a Random CityTrip")
        print("[2] View your Random CityTrip")
        print("[3] Exit\n")

        try:
            selection = int(input("YOUR SELECTION: "))
        except ValueError:
            print("Only numbers please")
        else:
            command = selection
            break

    if command == 1:
        make_reservation()
        menu()
    elif command == 2:
        open_pickled_reservation()
        menu()
    elif command == 3:
        print("Thank you for using Random CityTrip!")
        return
    else:
        print("Please select a number from 1 to 3")
        menu()


def make_reservation():
    customer = ask_name()
    destination = select_destination()
    print(f"Your randomly selected destination is: {destination.city}")

    while True:
        try:
            vehicle = select_vehicle()
            print(f"You've selected a {vehicle.vtype}")
            if vehicle.vtype == 'bicycle':
                vehicle.cycle()
            elif vehicle.vtype == 'car':
                vehicle.drive()
            elif vehicle.vtype == 'boat':
                vehicle.sail()
            elif vehicle.vtype == 'hovercraft':
                vehicle.drive()
                vehicle.sail()
            elif vehicle.vtype == 'train':
                vehicle.ride()
            elif vehicle.vtype == 'airplane':
                vehicle.fly()
        except:
            print("Please try again")
        else:
            break

    price = vehicle.km_cost * destination.distance
    reservation = Reservation(customer.name, destination.city, destination.distance, vehicle.vtype, price)

    write_to_file(reservation)
    pickle_to_file(reservation)

    return reservation


def ask_name():
    booker = input("Provide booker name: ")
    customer = Customer(booker)
    return customer


def select_destination():
    cities = {'London': 539, 'Lissabon': 2237, 'Brussel': 206, 'Berlin': 663, 'Barcelona': 1539}
    city, distance = choice(list(cities.items()))
    destination = Destination(city, distance)
    return destination


def select_vehicle():
    while True:
        print("\nSELECT A VEHICLE")
        print("[1] Bicycle")
        print("[2] Car")
        print("[3] Boat")
        print("[4] Hovercraft")
        print("[5] Train")
        print("[6] Airplane\n")

        try:
            selection = int(input("YOUR SELECTION: "))
        except ValueError:
            print("Only numbers please")
        else:
            command = selection
            break

    if command == 1:
        return Bicycle.add_to_reservation()

    elif command == 2:
        return Car.add_to_reservation()

    elif command == 3:
        return Boat.add_to_reservation()

    elif command == 4:
        return Hovercraft.add_to_reservation()

    elif command == 5:
        return Train.add_to_reservation()

    elif command == 6:
        return Airplane.add_to_reservation()

    else:
        print("Please select a number from 1 to 6")


def write_to_file(reservation):
    while True:
        print("\nDo you want to save a copy of your reservation for your administration? Y/N")
        try:
            selection = str(input("YOUR SELECTION: "))
        except ValueError:
            print("Only a letter please")
        else:
            command = selection
            break

    if command.upper() == 'Y':
        try:
            with open('reservation.txt', 'w') as file:
                file.write("YOUR RANDOM CITYTRIP RESERVATION\n")
                file.write(f"Name: {reservation.customer}\n")
                file.write(f"City: {reservation.city}\n")
                file.write(f"Distance from Amsterdam: {reservation.distance}km\n")
                file.write(f"Vehicle: {reservation.vehicle}\n")
                file.write(f"Price: \u20ac{reservation.price}")
        except:
            print("Couldn't save your file")
        else:
            print("File was successfully saved")
        read_file()
    elif command.upper() == 'N':
        return
    else:
        print("Please select Y or N")
        write_to_file(reservation)


def read_file():
    try:
        with open('reservation.txt') as file:
            content = file.read()
            print(f"\nThe content of your saved file:\n"
                  f"{content}")
    except:
        print("Couldn't read the file")


def pickle_to_file(reservation):
    try:
        with open('reservation.pickle', 'wb') as file:
            pickle.dump(reservation, file)
    except:
        print("Couldn't pickle the Reservation object")


def open_pickled_reservation():
    try:
        with open('reservation.pickle', 'rb') as file:
            reservation = pickle.load(file)
            print(reservation)
    except:
        print("You have no Random CityTrip")




