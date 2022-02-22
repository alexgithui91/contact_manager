import sqlite3
import time
import sys
import os.path
import psycopg2
from os import path
from db_connector import connect


def initiate_db():
    """[summary]"""
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
        conn.commit()
        print("Contacts table created.")


def create_contact():
    """[summary]"""
    if path.exists("contacts_file.csv"):
        conn, cur = connect()

        sql_query = "COPY tbl_contacts(first_name,last_name,phonenumber,email) FROM '\contacts_file.csv' DELIMITER ',' CSV HEADER;"

        cur.execute(sql_query)

        conn.commit()
    else:
        print("Contact File Not Found.")


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
    create_contact()


if __name__ == "__main__":
    main()
