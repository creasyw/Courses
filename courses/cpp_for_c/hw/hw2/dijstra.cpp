#include <iostream>
#include <vector>
#include <stdlib.h>
#include "dijstra.h"
#include "minheap.h"

using namespace std;

graph::graph(int n) {
    num = n;
    arr = new int*[num];
    for (int i=0; i<num; ++i)
        arr[i] = new int[num];
}

// return number of vertices
int graph::num_of_vertices() {
    return num;
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
void graph::add (int x, int y, int val) {
    check(x, -1, num-1, "index of vertex is out of range");
    check(y, -1, num-1, "index of vertex is out of range");

    if (arr[x][y] > 0 || x == y) return;
    arr[x][y] = arr[y][x] = val;
}

// removes the edge from x to y, if it is there
void graph::remove (int x, int y) {
    arr[x][y]=0;
}

// display matrix in a row/col format
void graph::display_matrix(){
    for (int i=0; i < num; ++i) {
        for (int j=0; j < num; ++j)
        cout<< arr[i][j] << " ";
        cout << endl;
    }
}

void graph::directed_matrix(float density, int lrange, int urange) {
    check(density, 0, 1, "Density should be in (0,1]");
    check(lrange, 0, urange, "The ranges is 0 < lrange< urange");

    int nedge = static_cast<int>(num*(num-1)*density);
    int count = 0;
    cout << nedge << endl;
    while (count < nedge) {
        srand(clock());
        int col = rand() % num;
        int row = rand() % num;
        // if the route has been set, it doesn't need to set again.
        // Or, there is no sense to set diagonal elements
        if (arr[row][col] > 0 || row == col)
            continue;
        int val = rand() % (urange - lrange + 1) + lrange;
        arr[row][col] = val;
        count++;
    }
}

// The undirected matrix has the same value for both [i,j] and [j,i]
void graph::undirected_matrix(float density, int lrange, int urange) {
    check(density, 0, 1, "Density should be in (0,1]");
    check(lrange, 0, urange, "The ranges is 0 < lrange< urange");

    int nedge = static_cast<int>(num*(num-1)/2*density);
    cout << num*(num-1)/2 << endl;
    cout << nedge << endl;
    int count = 0;
    while (count < nedge) {
        srand(clock());
        int row = rand() % num;
        int col = rand() % (num-row);
        // if the route has been set, it doesn't need to set again.
        // Or, there is no sense to set diagonal elements
        if (arr[row][col] > 0 || row == col)
            continue;
        int val = rand() % (urange - lrange + 1) + lrange;
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

class dijstra {
    public:
        dijstra(int n) {
            path_cost = -1;
        }
        vector<int> path(minheap candidates, graph g, int u, int v) {
            vector<int> result;
            path_cost = 0;
            int begin = u;
            int next = -1;
            while (candidates.size()!=0) {
                heapitem t = candidates.pop();
                int node = t.get_node();
                result.push_back(node);
                path_cost += t.get_key();
                if (node == v)
                    return result;
                vector<int> n = g.neighbors(node);

                for(vector<int>::iterator i=n.begin(); i!=n.end(); ++i) {
                    candidates.update(g.cost(node,*i), *i);
                }
            }
            // after iteration, the v is not found
            vector<int> r;
            return r;
        }

        float path_size(minheap c, graph g, int u, int v) {
            vector<int> p = path(c, g, u, v);
            if (p.size()!=0)
                return path_cost;
            else
                return -1;
        }

    private:
        float path_cost;
};

void test_graph() {
    int n = 10;
    graph test(n);
    cout << "After initialization:" << endl;
    test.display_matrix();
    cout << "\nAfter generate:" << endl;
    test.undirected_matrix(0.5, 5, 10);
    test.display_matrix();
    cout << test.num_of_vertices() << endl;
    cout << test.num_of_edges() << endl;

    cout << "Test function neighbor(5): " << endl;
    vector<int> hit = test.neighbors(5);
    for( vector<int>::const_iterator i = hit.begin(); i != hit.end(); ++i)
            cout << *i << ' ';
    cout << "\n" << endl;

    cout << "Test adjancent function for node 2" << endl;
    for (int i=0; i<n; ++i) {
        cout << test.adjancent(2,i) << " ";
    }
    cout << "\n" << endl;

    cout << "Test add all edges connected node 2" << endl;
    for (int i=0; i<n; ++i) {
        test.add(2,i, 20);
    }
    test.display_matrix();
    cout << "" << endl;

    cout << "Test delete all edges connected node 2" << endl;
    for (int i=0; i<n; ++i) {
        test.remove(2,i);
    }
    test.display_matrix();
}

int main()
{

}

