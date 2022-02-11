import sqlite3
import time
import sys
from db_connector import connect

# This should check if ContactsManager DB exists. If not create it
# This should check if Contacts Table exists. If not create it
def initiate_db():
    conn = connect()
    print(conn)


def create_contact():
    """[summary]"""
    print("You are in create function")


def retrieve_contact():
    """[summary]"""
    print("You are in retrieve function")


def update_contact():
    """[summary]"""
    print("You are in update function")


def delete_contact():
    """[summary]"""
    print("You are in delete function")


def main():
    initiate_db()


if __name__ == "__main__":
    main()
