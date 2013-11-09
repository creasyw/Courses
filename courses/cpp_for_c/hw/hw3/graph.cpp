#include <iostream>
#include <fstream>
#include <vector>
#include<algorithm>
#include <map>

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

graph::graph(string filename) {
    ifstream data(filename);
    if (!data) {
        cerr << "Cannot open file: " << filename << endl;
        exit (EXIT_FAILURE);
    }
    int num_of_nodes;
    data >> num_of_nodes;
    new (this) graph(num_of_nodes);
    vector<float> matrix;
    std::copy(std::istream_iterator<float>(data), 
        std::istream_iterator<float>(), std::back_inserter(matrix));
    // get rid of other redundant info at the beginning of data
    int offset = matrix.size() % 3;
    for (vector<float>::iterator i=matrix.begin()+offset;
        i!=matrix.end(); i+=3) {
        int row = static_cast<int>(*i);
        int col = static_cast<int>(*(i+1));
        check(row, -1, num-1, "index of vertex is out of range");
        check(col, -1, num-1, "index of vertex is out of range");
        arr[row][col] = arr[col][row] = *(i+2);
    }
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


class union_find {
    public:
        inline int num_of_unions() {
          return leader.size();
        }
        // check if one node has already been explored
        // if it is, return the leader element
        int find(int i) {
            map<int, int>::iterator it = nodes.find(i);
            if (it == nodes.end())
                return -1;
            return it->second;
        }
        void unions(int l1, int l2) {
            vector<int> temp = leader[l2];
            for(vector<int>::iterator it=temp.begin(); it!=temp.end(); ++it)
                nodes[*it] = l1;
            leader[l1].insert(leader[l1].begin(),leader[l2].begin(),leader[l2].end());
            leader.erase(l2);
        }
        // the input two nodes i and j are presumed having different leaders
        void insert(int i, int j) {
            int l1 = find(i);
            int l2 = find(j);
            if (l1!=-1 && l2!=-1)
                unions(min(l1, l2) ,max(l1, l2));
            else if(l1!=-1) {
                nodes[j] = l1;
                leader[l1].push_back(j);
            } else if(l2!=-1) {
                nodes[i] = l2;
                leader[l2].push_back(i);
            } else {
                int l = min(i,j);
                nodes[i] = l;
                nodes[j] = l;
                leader[l] = vector<int>();
                leader[l].push_back(i);
                leader[l].push_back(j);
            }
        }
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
        void prim(graph g) {
            int num = g.num_of_vertices();
            minheap* candidates = new minheap(num);
            reset();

            // find the starting point and initialize the heap
            int start_node = 0;
            while(candidates->size() == 0) {
                for(int i=0; i<num; ++i) {
                    float c = g.cost(start_node, i);
                    if (c != 0) candidates->update(c, i);
                }
                ++start_node;
            }
            closed_set.insert(start_node-1);

            while (candidates->size()!=0) {
                heapitem t = candidates->pop();
                int node = t.get_node();
                // not record the duplicated probed nodes
                if (closed_set.find(node)!=closed_set.end())
                    continue;
                closed_set.insert(node);
                path_cost += t.get_key();
                vector<int> n = g.neighbors(node);
                // update the heap with newly found nodes and edges
                for(vector<int>::iterator i=n.begin(); i!=n.end(); ++i) {
                    candidates->update(g.cost(node,*i), *i);
                }
            }
            // ckeck if there are isolated nodes
            if (closed_set.size() < num-1) path_cost=-1;
        }

        static bool kruskal_compare(vector<float>& v1, vector<float>& v2) {
            return v1.back() < v2.back();
        }

        void kruskal(graph g) {
            int num = g.num_of_vertices();
            vector< vector<float> > edges;
            union_find explored;
            reset();

            // put all connected vertices in "edges"
            for(int i=0; i<num; ++i) {
                for(int j=0; j<num; ++j) {
                    float c = g.cost(i, j);
                    if (c!=0) {
                        vector<float> temp;
                        temp.push_back(i);
                        temp.push_back(j);
                        temp.push_back(c);
                        edges.push_back(temp);
                    }
                }
            }
            sort(edges.begin(), edges.end(), kruskal_compare);

            for(vector<vector<float> >::iterator  p=edges.begin(); p!=edges.end(); ++p) {
                // both nodes in the closed set ==> detecting a cycle
                vector<float> temp = *p;
                int f1 = explored.find(temp[0]);
                int f2 = explored.find(temp[1]);
                if(f1!=-1 && f2!=-1 && f1==f2) continue;
                path_cost += temp[2];
                explored.insert(temp[0], temp[1]);
                //cout <<"From "<<temp[0]<<" To "<<temp[1]<<" -- Cost "<<temp[2]<<endl;
            }
            // ckeck if there are isolated nodes
            if (explored.num_of_unions() != 1) path_cost=-1;
        }


        float path_via_prime(graph g) {
            prim(g);
            return path_cost;
        }

        float path_via_kruskal(graph g) {
            kruskal(g);
            return path_cost;
        }

    private:
      // storing the sum of cost
      float path_cost;
      // storing nodes that have been explored
      set<int> closed_set;
};


int main(int argc, char* argv[]) {
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " File_Name" << endl;
        return 1;
    }
    
    graph g(argv[1]);
    mst m;
    cout << m.path_via_prime(g) << endl;
    cout << m.path_via_kruskal(g) << endl;

}

