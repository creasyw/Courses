# Karger minimum cut algorithm
# Returns the minimum number of cuts in a connected graph
import re
import random
import copy

#Download the text file here. Zipped version here. (Right click and save link as)
#The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646
#
#Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph. 
#
#Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0".
#
#WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.



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
