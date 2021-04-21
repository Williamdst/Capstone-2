import logging
import pkg_resources
from postman_problems.solver import cpp
from postman_problems.stats import calculate_postman_solution_stats

def main():
    EDGELIST = pkg_resources.resource_filename('postman_problems',
                                               'examples/sleeping_giant/edgelist_sleeping_giant.csv')
    NODELIST = pkg_resources.resource_filename('postman_problems',
                                               'examples/sleeping_giant/nodelist_sleeping_giant.csv')
    START_NODE = "b_end_east"

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('Solve CPP')
    circuit, graph = cpp(EDGELIST, START_NODE)

    logger.info('Print the CPP Solution')
    for e in circuit:
        logger.info(e)

    logger.info('Solution Summary Stats')
    for k,v in calculate_postman_solution_stats(circuit).items():
        logger.info(str(k) + ' : ' + str(v))


if __name__ == '__main__':
    main()