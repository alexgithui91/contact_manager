import sqlite3
import time
import sys

DB_FILE = "db_contacts.db"

# This should check if ContactsManager DB exists. If not create it
# This should check if Contacts Table exists. If not create it
def create_db():
    """[summary]"""
    pass


def create_contact():
    """[summary]"""
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    phone_number = input("Enter Phonenumber: ")
    email = input("Enter Email: ")

    try:
        conn = sqlite3.connect(DB_FILE)
        conn.execute(
            "INSERT INTO contacts_list (f_name, l_name, phone_number, email) VALUES (?,?,?,?)",
            (f_name, l_name, phone_number, email),
        )
        conn.commit()
        conn.close()
    except sqlite3.Error as er:
        print("Error: ", er)

    retrieve_contact()


def retrieve_contact():
    """[summary]"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.execute("SELECT * FROM contacts_list")
        for row in cur:
            print(row)
        conn.close()
    except sqlite3.Error as er:
        print("Error: ", er)


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
