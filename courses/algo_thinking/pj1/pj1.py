"""
Project one
"""

import alg_module1_graphs

# Representing directed graphs
EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}

EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes
    """
    result = {}
    if num_nodes <= 0:
        return result
    for index in range(num_nodes):
        result[index] = set([node for node in range(num_nodes) if node!=index])
    return result

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph.
    """
    result = {}
    for key in digraph:
        result[key] = 0
    for key in digraph:
        for val in digraph[key]:
            result[val] += 1
    return result

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a resultionary) and computes
    the unnormalized distribution of the in-degrees of the graph.
    """
    in_degree = compute_in_degrees(digraph)
    result = {}
    for _, val in in_degree.iteritems():
        if val in result:
            result[val] += 1
        else:
            result[val] = 1
    return result

#print compute_in_degrees(EX_GRAPH0)
#print compute_in_degrees(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
#print in_degree_distribution(alg_module1_graphs.GRAPH0)
