import logging
import itertools
import sqlite3
import pandas as pd
from postman_problems.solver import no_return_cpp
from postman_problems.stats import calculate_postman_solution_stats
import database_functions as dbfun
import postman_problems.graph as ppg
import os


def main():
    # Connect to the Mongo & create collection
    subwayDB = dbfun.create_subway_mongodb()
    route_collection = subwayDB.routes
    clear_mongo_db = True

    # Connect to Sqlite3 & create table
    sqlite3_conn = dbfun.create_subway_sqlite3(clear_db=True)

    EDGELIST = './Data/Paths-Decision-Points.csv'

    el = ppg.read_edgelist(EDGELIST, keep_optional=False)
    g = ppg.create_networkx_graph_from_edgelist(el)

    odd_nodes = ppg.get_odd_nodes(g)

    # This for loop gets all the euler paths for every combination of start and end nodes,
    # saves the routes/statistics as a dictionary, and appends it to the path_stats list
    for odd_node_pair in itertools.combinations(odd_nodes, 2):
        START_NODE = odd_node_pair[0]
        END_NODE = odd_node_pair[1]
        circuit_name = odd_node_pair[0] + ' - ' + odd_node_pair[1]

        path_stats = {'path':circuit_name}

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(f'Solved CPP for {circuit_name}')

        # For some reason, the no_return_cpp is returning the path backwards so the end_node is passed as the start
        circuit, graph = no_return_cpp(EDGELIST, END_NODE, START_NODE)

        # Formats the route and adds it to the dictionary along with the other stats
        route = '-'.join([edge[0] for edge in circuit])
        route = route + '-' + END_NODE
        path_stats.update(calculate_postman_solution_stats(circuit))
        path_stats['route'] = route

        # Inserts the path_stats into mongodb
        if clear_mongo_db == True:
            dbfun.insert_into_mongo(path_stats, route_collection, clear_db=clear_mongo_db)
            clear_mongo_db = False
        else:
            dbfun.insert_into_mongo(path_stats, route_collection, clear_db=False)

        # Inserts into Sqlite3
        dbfun.insert_into_sqlite3(sqlite3_conn, path_stats)

def query_db():
    conn = sqlite3.connect('SubwayChallenge.db')
    cursor = conn.cursor()

    query = input('Enter Query or -1 to Exit: \n')

    if query == '-1':
        print('Exiting Application')
        return False
    else:
        try:
            cursor.execute(query)
            colnames = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns = colnames)
            print(df)
            return True
        except:
            query_db()

if __name__ == '__main__':
    # Set to True to create databases (~20m)
    run_main = False
    if run_main:
        main()
    else:
        continue_query = True
        while continue_query :
            continue_query = query_db()