#include <vector>
#include <algorithm>
#include <map>

#include "mst.h"
#include "graph.h"
#include "minheap.h"

using namespace std;

// check if one node has already been explored
// if it is, return the leader element
int union_find::find(int i) {
    map<int, int>::iterator it = nodes.find(i);
    if (it == nodes.end())
        return -1;
    return it->second;
}
void union_find::unions(int l1, int l2) {
    vector<int> temp = leader[l2];
    for(vector<int>::iterator it=temp.begin(); it!=temp.end(); ++it)
        nodes[*it] = l1;
    leader[l1].insert(leader[l1].begin(),leader[l2].begin(),leader[l2].end());
    leader.erase(l2);
}
// the input two nodes i and j are presumed having different leaders
void union_find::insert(int i, int j) {
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

void mst::prim(graph g) {
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

bool mst::kruskal_compare(vector<float>& v1, vector<float>& v2) {
    return v1.back() < v2.back();
}

void mst::kruskal(graph g) {
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


float mst::path_via_prime(graph g) {
    prim(g);
    return path_cost;
}

float mst::path_via_kruskal(graph g) {
    kruskal(g);
    return path_cost;
}


