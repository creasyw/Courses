#include <vector>
#include <map>
#include "union_find.h"

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

