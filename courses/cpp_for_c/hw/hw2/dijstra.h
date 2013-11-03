#ifndef DIJSTRA_H
#define DIJSTRA_H

#include "dijstra.h"
#include "minheap.h"

class graph{
    public:
        graph(int n);
        // return number of vertices
        int num_of_vertices();
        int num_of_edges();
        float cost(int x, int y);
        bool adjancent(int x, int y);
        std::vector<int> neighbors(int x);
        void add (int x, int y, float val);
        void remove (int x, int y);
        void display_matrix();
        void directed_matrix(float density, float lrange, float urange);
        void undirected_matrix(float density, float lrange, float urange);

    private:
        int num;
        float**  arr;
        void check(float target, int lower, int upper, std::string e);
};

class dijstra {
    public:
        dijstra();
        std::vector<int> path(minheap* candidates, graph g, int u, int v);
        float path_size(minheap* c, graph g, int u, int v);

    private:
        float path_cost;
};

#endif
