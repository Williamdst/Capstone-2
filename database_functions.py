import sqlite3
import pymongo
import os


def create_subway_sqlite3(clear_db=False):
    if 'SubwayChallenge.db' not in os.listdir():
        conn = sqlite3.connect('SubwayChallenge.db')
        cursor = conn.cursor()
    elif clear_db:
        os.remove('SubwayChallenge.db')
        conn = sqlite3.connect('SubwayChallenge.db')
        cursor = conn.cursor()
    else:
        conn = sqlite3.connect('SubwayChallenge.db')
        cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes(
            path VARCHAR(10),
            distance_walked SMALLINT,
            distance_doublebacked SMALLINT,
            distanced_walked_once SMALLINT,
            distance_walked_optional SMALLINT,
            distance_walked_required SMALLINT,
            edges_walked SMALLINT,
            edges_doublebacked SMALLINT,
            edges_walked_once SMALLINT,
            edges_walked_optional SMALLINT,
            edges_walked_required SMALLINT,
            route VARCHAR
        );"""
    )
    conn.commit()
    return conn


def insert_into_sqlite3(conn, dict_of_values):
    with conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO routes VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                       [dict_of_values['path'],
                        dict_of_values['distance_walked'],
                        dict_of_values['distance_doublebacked'],
                        dict_of_values['distance_walked_once'],
                        dict_of_values['distance_walked_optional'],
                        dict_of_values['distance_walked_required'],
                        dict_of_values['edges_walked'],
                        dict_of_values['edges_doublebacked'],
                        dict_of_values['edges_walked_once'],
                        dict_of_values['edges_walked_optional'],
                        dict_of_values['edges_walked_required'],
                        dict_of_values['route']
                        ])
        conn.commit()

    return print(f"Inserted Row for {dict_of_values['path']} and its Statistics into routes table")

def create_subway_mongodb():
    client = pymongo.MongoClient('localhost', 27017)

    if 'SubwayChallenge' not in client.list_database_names():
        subwayDB = client.SubwayChallenge
        return subwayDB
    else:
        return client.SubwayChallenge


def insert_into_mongo(document_dict, collection, clear_db=False):
    if clear_db == True:
        collection.delete_many({})

    collection.insert_one(document_dict)

    return print(f"Inserted Document for Path {document_dict['path']} and its Statistics into {collection}")
