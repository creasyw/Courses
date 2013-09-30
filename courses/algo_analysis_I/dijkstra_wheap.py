#given program demonstrates the working model of Dijkstras algorithm
from collections import defaultdict
import heapq

graph = defaultdict(dict)
file_handle = open("hw5_test_case2.txt", "r")
for line in file_handle:
    node = int(line.split()[0])
    graph[node] = {}
    for i in line.split()[1:]:
        edge = int(i.split(",")[0])
        weight = int(i.split(",")[1])
        graph[node][edge] = weight


def heap_update (heap, index, node, cost):
    """ The data in the heap is [cost, node]
    so that the heap is aranged according to the cost"""
    if node in index and cost < index[node]:
        heap.remove([index[node], node])
        heapq.heappush(heap, [cost, node])
        index[node] = cost
    elif node not in index:
        heapq.heappush(heap, [cost, node])
        index[node] = cost

def heap_pop(heap, index):
    cost, node = heapq.heappop(heap)
    index.pop(node)
    return node, cost

def dijkstras(graph, start):
    # keep a record of the distance of the nodes from the start vertex
    distance = defaultdict()
    # keep track of the candidates for the next move
    index = defaultdict()
    # store the cost and node into heap using cost as the key
    heap = []
    heapq.heapify(heap)
    #will be used to trace the path of the sjortest distance to each node
    distance[start] = 0
    if start in graph:
        for (node, cost) in graph[start].items():
            heap_update(heap, index, node, cost)
    else:
        return distance
    #initially all nodes are yet to be explored
    while len(index) > 0:
        # need to extract the node with the minimum path
        node, cost = heap_pop(heap, index)
        # store the node into known graph
        distance[node] = cost
        # update the knowledge according to existing node
        if node in graph:
            for (node, localcost) in graph[node].items():
                if node not in distance:
                    heap_update(heap, index, node, localcost+cost)
    return distance
distance = dijkstras(graph, 1)
print distance

#answer = []
#question = [7,37,59,82,99,115,133,165,188,197]
#for value in question:
#    answer.append(distance[value])
#print answer    
