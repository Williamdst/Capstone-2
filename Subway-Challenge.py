import logging
import itertools
from postman_problems.solver import no_return_cpp
from postman_problems.stats import calculate_postman_solution_stats
from Scripts import database_functions as dbfun
import postman_problems.graph as ppg

def main():
    # Connect to Sqlite3 & create table
    sqlite3_conn = dbfun.create_subway_sqlite3(clear_db=True)
    dbfun.add_stations_table_sqlite3(sqlite3_conn)
    dbfun.add_edges_table_sqlite3(sqlite3_conn)

    edgelist = './Data/Paths-Decision-Points.csv'

    el = ppg.read_edgelist(edgelist, keep_optional=False)
    g = ppg.create_networkx_graph_from_edgelist(el)

    odd_nodes = ppg.get_odd_nodes(g)

    # This for loop gets all the euler paths for every combination of start and end nodes,
    # saves the routes/statistics as a dictionary, and inserts it into the database
    for odd_node_pair in itertools.combinations(odd_nodes, 2):
        circuit_name = odd_node_pair[0] + ' - ' + odd_node_pair[1]

        path_stats = {'path': circuit_name}

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(f'Solved CPP for {circuit_name}')

        # For some reason, the no_return_cpp is returning the path backwards so the end_node is passed as the start
        circuit, graph = no_return_cpp(edgelist, odd_node_pair[1], odd_node_pair[0])

        # Formats the route and adds it to the dictionary along with the other stats
        route = '-'.join([edge[0] for edge in circuit])
        route = route + '-' + odd_node_pair[1]
        path_stats.update(calculate_postman_solution_stats(circuit))
        path_stats['route'] = route

        # Inserts into Sqlite3
        dbfun.insert_into_sqlite3(sqlite3_conn, path_stats)

    # Add rankings
    dbfun.add_route_ranks(sqlite3_conn)


# Set to True to Create the Database (~20m)
# Otherwise Load SubwayChallenge.db into SQLite
run_main = True
if __name__ == '__main__' and run_main:
    main()
