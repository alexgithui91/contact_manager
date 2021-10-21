import sqlite3
import time
import sys

DB_FILE = "db_contacts.db"


def create_contact():
    """[summary]"""
    pass


def retrieve_contact():
    """[summary]"""
    pass


def update_contact():
    """[summary]"""
    pass


def delete_contact():
    """[summary]"""
    pass


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
                print("go to create contact")
            elif int(selection) == 2:
                print("go to retrieve contact")
            elif int(selection) == 3:
                print("go to update contact")
            elif int(selection) == 4:
                print("go to delete contact")
        else:
            print("Error: Selection Out of Range")
    else:
        print("Error: Invalid Input")


if __name__ == "__main__":
    main()
