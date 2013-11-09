#ifndef MST_H
#define MST_H

#include<map>
#include "mst.h"
#include "graph.h"

using namespace std;

// data structure used in Kruskal's algorithm
class union_find {
    public:
        inline int num_of_unions() {return leader.size();}
        int find(int i);
        void unions(int l1, int l2);
        void insert(int i, int j);
    private:
        // the 1st element is the node, and the 2nd is the leader of cluster
        map<int, int> nodes;
        // the 1st element is the leader, and the 2nd are the nodes
        map<int, vector<int> > leader;
};

class mst{
    public:
        inline mst() {path_cost=0;}
        inline void reset() {
            path_cost = 0;
            closed_set.clear();
        }
        void prim(graph g);
        static bool kruskal_compare(vector<float>& v1, vector<float>& v2);
        void kruskal(graph g);
        float path_via_prime(graph g);
        float path_via_kruskal(graph g);

    private:
      // storing the sum of cost
      float path_cost;
      // storing nodes that have been explored
      set<int> closed_set;
};

#endif
