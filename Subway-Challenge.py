import logging
import itertools
from postman_problems.solver import no_return_cpp
from postman_problems.stats import calculate_postman_solution_stats
import mongo_functions as mdb
import postman_problems.graph as ppg



def main():
    # Connect to the Database & create collection
    subwayDB = mdb.create_subway_mongodb()
    route_collection = subwayDB.routes

    EDGELIST = './Data/Paths-Decision-Points.csv'

    el = ppg.read_edgelist(EDGELIST, keep_optional=False)
    g = ppg.create_networkx_graph_from_edgelist(el)

    odd_nodes = ppg.get_odd_nodes(g)
    clear_mongo_db = True

    # This for loop gets all the euler paths for every combination of start and end nodes,
    # saves the routes/statistics as a dictionary, and appends it to the path_stats list
    for odd_node_pair in itertools.combinations(odd_nodes, 2):
        START_NODE = odd_node_pair[0]
        END_NODE = odd_node_pair[1]
        path_stats = {'path':START_NODE + ' - ' + END_NODE}

        circuit_name = odd_node_pair[0] + ' - ' + odd_node_pair[1]

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        logger.info(f'Solved CPP for {circuit_name}')

        # For some reason, the no_return_cpp is returning the path backwards so the end_node is passed as the start
        circuit, graph = no_return_cpp(EDGELIST, END_NODE, START_NODE)

        route = '-'.join([edge[0] for edge in circuit])
        route = route + '-' + END_NODE
        path_stats.update(calculate_postman_solution_stats(circuit))
        path_stats['route'] = route

        if clear_mongo_db == True:
            mdb.insert_into_mongo(path_stats, route_collection, clear_db=clear_mongo_db)
            clear_mongo_db = False
        else:
            mdb.insert_into_mongo(path_stats, route_collection, clear_db=False)

if __name__ == '__main__':
    main()