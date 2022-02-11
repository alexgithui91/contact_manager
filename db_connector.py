import psycopg2
from config import config


def connect():
    """Connect to PostgreSQL DB Server"""
    conn = None

    try:
        # read connection params
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn, cur
