#given program demonstrates the working model of Dijkstras algorithm
from collections import defaultdict
import heapq


def heap_update(heap, index, node, cost):
    """ The data in the heap is [cost, node]
    so that the heap is aranged according to the cost"""
    if node in index and cost < index[node]:
        heap.remove([index[node], node])
        heap.append([cost, node])
        heapq.heapify(heap)
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
    if start in graph and type(graph[start]) == dict:
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
        if node in graph and type(graph[node]) == dict:
            for (node, localcost) in graph[node].items():
                if node not in distance:
                    heap_update(heap, index, node, localcost + cost)
    return distance


def buildgraph(data):
    """ data is a dictionary { st1: [[st1, end1, cost1]... [st1, endn, costn]] ....
                               stn: [[stn, end1, costn]... [stn, endn, costn]]}
        the output is a matrix represented as 2-levels dictionary
                             { st1: {end1:cost1, end2:cost2 ... endn:costn} ...
                               stn: {end1:cost1, end2:cost2 ... endn:costn}}
        which can be the input of dijkstras algo.
    """
    for i in data:
        temp = data[i]
        data[i] = {}
        for j in temp:
            data[i][j[1]] = j[2]
    return data
