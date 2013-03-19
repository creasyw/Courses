from collections import defaultdict
import os

# The implementation of graph could be:
# dict{ node:{node:distance, node:distance,...}, node{,,,}...}
# distance: the value in the matrix, node: row*100+col
def build_graph(matrix):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-1):
            if j != 0:
                if i != 0 and i != len(matrix)-1:
                    graph[i*100+j] = {(i-1)*100+j:matrix[i-1][j], (i+1)*100+j:matrix[i+1][j], i*100+j+1:matrix[i][j+1]}
                elif i == 0:
                    graph[j] = {100+j:matrix[1][j], j+1:matrix[0][j+1]}
                else:
                    graph[i*100+j] = {(i-1)*100+j:matrix[i-1][j], i*100+j+1:matrix[i][j+1]}
            else:
                graph[i*100+j] = {i*100+j+1:matrix[i][j+1]}
    return graph

# Use the 1th column as starting candidates feeding into Dijkstra's Algorithm.
def gen_candidates(matrix):
    candidates = {}
    for i in range(len(matrix)):
        candidates[i*100] = matrix[i][0]
    return candidates

# According to the question, ending criterion is arriving at the right column.
def end_criterion(ending, candidate):
    return candidate in ending

# Note that the running time for Dijastra's algorithm is "almost" linear, which is equal to
# O(mlogn), where m is the # of edges and n is the # of vertices.
# The algorithm should be used for "weak link" graphs.
# The basic algorithm comes from Wikipedia http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# But there are some critical aspects missing in that article:
# 1. there should be a list keeping track of visited nodes, or it will visit the same node over and over again.
# 2. there are two other datasets: original graph and a priority queue
# 3. the algorithm tends to visit every node in the graph if possible. It is the"Traveling salesman problem".
# 4. if the goal is to find shortest path with given starting and ending points, just like this question. 
#    Keeping track of shortest distance from begining and returning the 1st hit of the ending point with 
#    accumulated distance should be fine.
def dijkstra(graph, candidates):
    ending = set(k*100+79 for k in range(80))
    visited = {}
    while candidates != {}:
        candidate = min(candidates, key=candidates.get)
        visited[candidate] =  candidates.get(candidate)
        del candidates[candidate]
        if end_criterion(ending, candidate):
            break
        for node in graph[candidate]:
            if node in visited:
                continue
            elif node in candidates:
                candidates[node] = min(candidates[node], visited[candidate]+graph[candidate][node])
            else:
                candidates[node] = visited[candidate]+graph[candidate][node]
    return visited[candidate]

def main():
    matrix = defaultdict(list)
    count = 0
    with  open(os.path.join(os.path.dirname(__file__), 'matrix.txt')) as matfile:
        for row in matfile:
            matrix[count] = [int(k) for k in row.split(',')]
            count += 1
    print dijkstra(build_graph(matrix), gen_candidates(matrix))

if __name__ == "__main__":
    main()

