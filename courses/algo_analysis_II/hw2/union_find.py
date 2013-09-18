from collections import defaultdict

class union_find:
    def __init__(self):
        """For the union find, the key is vertex 
        and the value is its leading vertex"""
        self.alldata = defaultdict()
        self.cluster = defaultdict(list)

    def init_dataset(self, npar):
        """ initialize the dataset with ndarray """
        vertex = set(list(npar[:,0])+list(npar[:,1]))
        for i in vertex:
            self.cluster[i] = [i]
            self.alldata[i] = i

    def find(self, k):
        if k in self.alldata:
            return self.alldata[k]
        else:
            return False
    
    def merge(self, c1, c2):
        lst = self.cluster.pop(c2)
        self.cluster[c1] += lst
        for i in lst:
            self.alldata[i] = c1
    
    def union(self, c1, c2):
        l1 = len(self.cluster[c1])
        l2 = len(self.cluster[c2])
        if l1 > l2:
            self.merge(c1, c2)
        else:
            self.merge(c2, c1)
    
    def is_circle(self, v1, v2):
        return self.alldata[v1] and self.alldata[v2] \
                and self.alldata[v1]==self.alldata[v2]

    def put(self, edge):
        """ the edge is [v1, v2, edge_cost] """
        f0 = self.find(edge[0])
        f1 = self.find(edge[1])
        if f0 and f1:
            if f1==f0:
                return
            else:
                self.union(f0, f1)
        elif f0:
            self.alldata[edge[1]] = f0
            self.cluster[f0].append(edge[1])
        elif f1:
            self.alldata[edge[0]] = f1
            self.cluster[f1].append(edge[0])
        else:
            self.alldata[edge[1]] = edge[0]
            self.alldata[edge[0]] = edge[0]
            self.cluster[edge[0]] = list(edge[:2])

    def length(self):
        return len(self.cluster)

    def display(self):
        return self.cluster

    def num_of_nodes(self):
        return len(self.alldata)
