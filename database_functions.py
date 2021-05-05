import sqlite3
import pandas as pd
import os


def create_subway_sqlite3(clear_db=False):
    if 'SubwayChallenge.db' in os.listdir() and clear_db:
        os.remove('SubwayChallenge.db')
        conn = sqlite3.connect('SubwayChallenge.db')
        cursor = conn.cursor()
    else:
        conn = sqlite3.connect('SubwayChallenge.db')
        cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes(
            path VARCHAR(10) PRIMARY KEY,
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


def add_stations_table_sqlite3(conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stations(
                stationid SMALLINT PRIMARY KEY,
                station VARCHAR,
                borough VARCHAR(12),
                lines VARCHAR,
                nodes VARCHAR
            );"""
        )

        df = pd.read_csv('./Data/Stations-Decision-Points.csv')
        df.to_sql('stations', conn, if_exists='replace', index=False)
        conn.commit()

    return None


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


def add_route_ranks(conn):
    with conn:
        cursor = conn.cursor
        cursor.execute("""
            UPDATE routes
            SET route_rank = ranking
            FROM (SELECT 
                    path, 
                    dense_rank() over (order by distance_walked) as ranking 
                  FROM routes
                  ) as ranking_query
            WHERE routes.path = ranking_query.path;
            """)
        conn.commit()
    return None