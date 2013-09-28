#given program demonstrates the working model of Dijkstras algorithm
from collections import defaultdict
import heapq

graph = defaultdict(dict)
file_handle = open("dijkstraData.txt", "r")
for line in file_handle:
    node = int(line.split()[0])
    graph[node] = {}
    for i in line.split()[1:]:
        edge = int(i.split(",")[0])
        weight = int(i.split(",")[1])
        graph[node][edge] = weight


def heap_update (heap, index, item):
    if item[0] in index and item[1] < index[item[0]]:
        heap.remove(index[item[0]])
        heapq.heappush(heap, item)
        index[item[0]] = item[1]
    elif item[0] not in index:
        heapq.heappush(heap, item)
        index[item[0]] = item[1]

def dijkstras(graph, start):
    #will keep a record of the distance of the nodes from the start vertex
    parent = {}
    distance = {}
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
    return distance
distance = dijkstras(graph, 1)

answer = []
question = [7,37,59,82,99,115,133,165,188,197]
for value in question:
    answer.append(distance[value])
print answer    
