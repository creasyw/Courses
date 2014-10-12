#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "dijkstra.h"
#include "minheap.h"
#include <set>

using namespace std;

class graph{
    public:
        graph(int n);
        inline int num_of_vertices() {return num;}
        int num_of_edges();
        float cost(int x, int y);
        bool adjancent(int x, int y);
        vector<int> neighbors(int x);
        void add (int x, int y, float val);
        void remove (int x, int y);
        void display_matrix();
        void directed_matrix(float density, float lrange, float urange);
        void undirected_matrix(float density, float lrange, float urange);

    private:
        int num;
        float**  arr;
        void check(float target, int lower, int upper, string e);
};

class dijkstra {
    public:
        inline dijkstra() {path_cost = -1;}
        inline void reset() {
            path_cost = -1;
            closed_set.clear();
        }
        void path(graph g, int u, int v);
        float path_size(graph g, int u, int v);

    private:
        float path_cost;
        set<int> closed_set;
};

#endif
