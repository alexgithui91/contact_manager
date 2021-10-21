import sqlite3
import time
import sys

DB_FILE = "db_contacts.db"


def create_contact():
    """[summary]"""
    print("Your are in create function")


def retrieve_contact():
    """[summary]"""
    print("Your are in retrieve function")


def update_contact():
    """[summary]"""
    print("Your are in update function")


def delete_contact():
    """[summary]"""
    print("Your are in delete function")


def main():
    """[summary]"""
    print("-- -- --> OPENING Contacts Book...")
    time.sleep(3)  # Sleep 3 seconds
    print("-- -- --> Contacts Book OPENED...")
    print("\n-- -- --> Please SELECT Operation:")
    print(
        """
        1. Create Contact
        2. Retrieve Contact
        3. Update Contact
        4. Delete Contact
        0. Quit
        """
    )

    selection = input("Enter selection: ")

    if selection.isdigit():
        if int(selection) in range(5):
            if int(selection) == 0:
                print("Contacts Book CLOSING...")
                time.sleep(3)  # Sleep 3 seconds
                print("Contacts Book CLOSED...")
                sys.exit()
            elif int(selection) == 1:
                create_contact()
            elif int(selection) == 2:
                retrieve_contact()
            elif int(selection) == 3:
                update_contact()
            elif int(selection) == 4:
                delete_contact()
        else:
            print("Error: Selection Out of Range")
    else:
        print("Error: Invalid Input")


if __name__ == "__main__":
    main()
