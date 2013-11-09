#include <iostream>
#include <vector>
#include <stdlib.h>
#include "graph.h"
#include "minheap.h"

using namespace std;

graph::graph(int n) {
    num = n;
    arr = new float*[num];
    for (int i=0; i<num; ++i)
        arr[i] = new float[num];
}

// This is specific for the undirected graph
int graph::num_of_edges() {
    int count = 0;
    for (int i=0; i < num-1; ++i)
        for (int j = i+1; j < num; ++j)
            if (arr[i][j] > 0) count++;
    return count;
}

float graph::cost(int u, int v) {
    check(u, -1, num-1, "index of vertex is out of range");
    check(v, -1, num-1, "index of vertex is out of range");
    return arr[u][v];
}

// tests whether there is an edge from node x to node y.
bool graph::adjancent(int x, int y) {
    check(x, -1, num-1, "index of vertex is out of range");
    check(y, -1, num-1, "index of vertex is out of range");
    return arr[x][y]>0;
}

// lists all nodes y such that there is an edge from x to y
vector<int> graph::neighbors(int x) {
    check(x, -1, num-1, "index of vertex is out of range");
    vector<int> result;
    for (int i=0; i<num; ++i) {
        if (arr[x][i] > 0) result.push_back(i);
    }
    return result;
}

// adds to G the edge from x to y with value val, if it does not exist
void graph::add (int x, int y, float val) {
    check(x, -1, num-1, "index of vertex is out of range");
    check(y, -1, num-1, "index of vertex is out of range");

    if (arr[x][y] > 0 || x == y) return;
    arr[x][y] = arr[y][x] = val;
}

// removes the edge from x to y, if it is there
void graph::remove (int x, int y) {
    check(x, -1, num-1, "index of vertex is out of range");
    check(y, -1, num-1, "index of vertex is out of range");
    arr[x][y]=0;
}

// display matrix in a row/col format
void graph::display_matrix(){
    for (int i=0; i < num; ++i) {
        for (int j=0; j < num; ++j)
        cout<< arr[i][j] << "\t";
        cout << endl;
    }
}

// The undirected matrix has the same value for both [i,j] and [j,i]
void graph::undirected_matrix(float density, float lrange, float urange) {
    check(density, 0, 1, "Density should be in (0,1]");
    check(lrange, 0, urange, "The ranges is 0 < lrange< urange");

    int nedge = static_cast<int>(num*(num-1)/2*density);
    int count = 0;
    while (count < nedge) {
        srand(clock());
        int row = rand()%(num-1);
        int col = (rand()%(num-1-row)) + row + 1;
        // if the route has been set, it doesn't need to set again.
        // Or, there is no sense to set diagonal elements
        if (arr[row][col] > 0)
            continue;
        float val = (float)rand()/((float)RAND_MAX/(urange-lrange)) + lrange;
        arr[row][col] = arr[col][row] = val;
        count++;
    }
}

// sanity check for arguments
//  The checking range is lower < target <= upper
void graph::check(float target, int lower, int upper, string e) {
    try {
        if (target <= lower || target > upper)
            throw invalid_argument(e);
    }
    catch (const invalid_argument& ia) {
        cerr << "Invalid argument: " << ia.what() << endl;
        exit (EXIT_FAILURE);
    }
}

int main()
{
    int n = 10;
    graph g(n);
    g.display_matrix();
    g.undirected_matrix(0.5, 1.0, 10.0);
    cout << "" << endl;
    g.display_matrix();
}

