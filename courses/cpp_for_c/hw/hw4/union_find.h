#ifndef UNIONFIND_H
#define UNIONFIND_H

#include<map>
#include<vector>
#include "union_find.h"

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

#endif
