# Karger minimum cut algorithm
# Returns the minimum number of cuts in a connected graph
import re
import random
import copy

# Establish source of graph
# Input format: First column of each row represents vertex label
# Each row tells all the vertices that the first vertex is adjacent to
source = "edges.txt"

# Number of iterations to search for lowest minimum cut
# Note: must run (n**2)*ln(n) to reduce failure to 1/n
n = 30

def minimum_cut(graph):
    if len(graph) < 3:
        return graph
    # Find a random edge, first by finding random vertice
    vertice = random.choice(graph.keys())
    # Then by finding random connection
    connection = graph[vertice][random.randrange(0,len(graph[vertice]))]
    while (connection in graph.keys()) == False:
        connection = graph[vertice][random.randrange(0,len(graph[vertice]))]
    # Now merge edge into single vertex
    graph[vertice] += graph[connection]
    del graph[connection]
    # And remove self-loops
    graph[vertice] = filter (lambda a: a != vertice, graph[vertice])
    graph[vertice] = filter (lambda a: a != connection, graph[vertice])
    # And replace all references to connection with reference to vertice
    for key, value in graph.iteritems():
        graph[key] = [x if x != connection else vertice for x in value]
    minimum_cut(graph)
    return graph

def get_graph():
    # Grabs graph from input file
    # Create dictionary with key for each node
    file = open(source)
    graph = {}
    for line in file:
        list = line.split()
        i = int(list[0])
        graph[i] = []
        for element in list[1:]:
            graph[i].append(int(element))
    file.close()
    return graph

def find_minimum_cuts():
    # Loop n times and display information from run with minimum cuts
    original = get_graph()
    for j in range(0,n): #This number of iterations may need to be increased
        graph = copy.deepcopy(original)
        minimum_cut(graph)
        count = 0
        for key, value in graph.iteritems():
            count += len(graph[key])
        count = count/2
        if j == 0:
            record_count = count
            record_iteration = j
        if count < record_count:
            record_count = count
            record_iteration = j
    return record_count,record_iteration

if __name__=="__main__":
    record_count, record_iteration = find_minimum_cuts()
    print "The minimum cut found within",n,"iterations is"
    print record_count,"connections found at iteration",record_iteration