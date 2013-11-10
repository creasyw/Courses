#ifndef GRAPH_H
#define GRAPH_H

#include "graph.h"
#include "minheap.h"
#include <set>

using namespace std;

class graph{
    public:
        graph(int n);
        graph(string filename);
        inline int num_of_vertices() {return num;}
        int num_of_edges();
        float cost(int x, int y);
        bool adjancent(int x, int y);
        vector<int> neighbors(int x);
        void add (int x, int y, float val);
        void remove (int x, int y);
        void display_matrix();
        void undirected_matrix(float density, float lrange, float urange);

    private:
        int num;
        float**  arr;
        void check(float target, int lower, int upper, string e);
};

#endif
