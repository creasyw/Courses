"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import matplotlib.pyplot as plt
import pj1
import numpy as np

###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def normailized_distr_graph(graph):
    distr = pj1.in_degree_distribution(graph)
    total = sum(distr[key] for key in distr)
    for key in distr:
        distr[key] = distr[key]/float(total)
    return distr

def directed_random_graph(num_nodes, prob):
    graph = {}
    if num_nodes <= 0:
        return graph
    for i in range(num_nodes):
        graph[i] = set([])
        for j in range(num_nodes):
            if i == j:
                continue
            if np.random.random() < prob:
                graph[i].add(j)
    return graph

def problem1():
    distr = normailized_distr_graph(load_graph(CITATION_URL))
    plt.loglog(distr.keys(), distr.values(), ".")
    plt.xlabel("Value of the in-degree")
    plt.ylabel("Possibilities for corresponding in-degree value")
    plt.title("In-degree Distribution for Citation Graph")
    plt.grid(True)
    plt.savefig("In-degree_distribution.pdf", format='pdf')
    plt.show()

def problem2():
    num_nodes = 200
    prob = 0.8
    distr = normailized_distr_graph(directed_random_graph(num_nodes, prob))
    plt.loglog(distr.keys(), distr.values(), ".")
    plt.xlabel("Value of the in-degree")
    plt.ylabel("Possibilities for corresponding in-degree value")
    plt.title("In-degree Distribution for Random Graph")
    plt.grid(True)
    plt.savefig("In-degree_distribution_ER.pdf", format='pdf')
    plt.show()


if __name__ == "__main__":
    problem2()
