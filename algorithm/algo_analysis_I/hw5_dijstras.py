#In this programming problem you'll code up Dijkstra's shortest-path algorithm. 
#Download the text file here. (Right click and save link as). 
#The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.
#
#Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000. 
#
#You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. Please type your answer in the space provided.
#
#IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

#given program demonstrates the working model of Dijkstras algorithm
from collections import defaultdict
distance = {}
graph = defaultdict(dict)
file_handle = open("dijkstraData.txt", "r")
for line in file_handle:
    node = int(line.split()[0])
    graph[node] = {}
    for i in line.split()[1:]:
        edge = int(i.split(",")[0])
        weight = int(i.split(",")[1])
        graph[node][edge] = weight


def dijkstras(graph, start):
    global distance
    #will keep a record of the distance of the nodes from the start vertex
    parent = {}
    #will be used to trace the path of the sjortest distance to each node
    for node in graph:
        distance[node] = float('inf')
        parent[node] = ""
    distance[start] = 0
    #origin point no need to travel
    unseen_nodes = graph.keys()
    #initially all nodes are yet to be explored
    while len(unseen_nodes) > 0:
        #need to extract the node with the minimum path
        shortest = None
        node = ""
        for temp in unseen_nodes:
            if shortest == None:
                shortest = distance[temp]
                node = temp
            #used to initialise the loop with a random value
            elif distance[temp] < shortest:
                shortest = distance[temp]
                node = temp
#  the first iteration of the while loop the start vertex will be 
#  discovered which will then be eventually removed after exploration 
#  of its neighbors
        unseen_nodes.remove(node)
        #removing the node with the lowest weight
        for (child, value) in graph[node].items():
            #will give the edge and weight of the path in the form of tupple 
            #here for each of the neighbors of the node we are relaxing the 
            #edges and giving the distance dict their respective weight value
            if (distance[child] > distance[node] + value):
                distance[child] = distance[node] + value
                parent[child] = node
                #relaxing the neighbors
dijkstras(graph, 1)

answer = []
question = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
for value in question:
    answer.append(distance[value])
print answer
