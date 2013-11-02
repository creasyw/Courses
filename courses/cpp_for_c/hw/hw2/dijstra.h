#ifndef DIJSTRA_H
#define DIJSTRA_H

#include "dijstra.h"
class graph{
    public:
        graph(int n);
        // return number of vertices
        int num_of_vertices();
        int num_of_edges();
        bool adjancent(int x, int y);
        std::vector<int> neighbors(int x);
        void add (int x, int y, int val);
        void remove (int x, int y);
        void display_matrix();
        void directed_matrix(float density, int lrange, int urange);
        void undirected_matrix(float density, int lrange, int urange);

    private:
        int num;
        int**  arr;
        void check(float target, int lower, int upper, std::string e);
};


#endif
