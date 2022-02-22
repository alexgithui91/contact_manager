import sqlite3
import time
import sys
from db_connector import connect


def initiate_db():
    conn, cur = connect()

    cur.execute(
        "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='tbl_contacts')"
    )

    result = cur.fetchone()[0]

    if result:
        print("Contacts table exists.")
    else:
        cur.execute(
            """
                CREATE TABLE tbl_contacts(
                contact_key SERIAL PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                phonenumber TEXT,
                email TEXT	
                );
            """
        )
        cur.close()
        conn.commit()


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
