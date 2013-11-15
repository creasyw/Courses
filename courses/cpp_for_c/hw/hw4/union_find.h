#ifndef UNIONFIND_H
#define UNIONFIND_H

#include <unordered_map>
#include <vector>
#include "union_find.h"

using namespace std;

// data structure used in Kruskal's algorithm
class union_find {
    public:
        inline union_find(int n): last(n) {}
        inline int num_of_unions() {return leader.size();}
        int found(int i);
        void unions(int l1, int l2);
        bool insert(vector<int> n, vector<int> ns, int p);
        void print();
    private:
        int last;
        // the 1st element is the node, and the 2nd is the leader of cluster
        unordered_map<int, int > nodes;
        // the 1st element is the leader, and the 2nd are the nodes
        unordered_map<int, vector<int> > leader;
};

#endif
