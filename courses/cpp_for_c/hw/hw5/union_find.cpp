#include <vector>
#include <iostream>
#include <unordered_map>
#include "union_find.h"

using namespace std;

// check if one node has already been explored
// if it is, return the leader element
int union_find::found(int i) {
    unordered_map<int, int>::iterator it = nodes.find(i);
    if (it == nodes.end())
        return -1;
    return it->second;
}

union_find::union_find(union_find& u):union_find(u.get_last()) {
    nodes = u.nodes;
    leader = u.leader;
}

// merge nodes with leader of l2 to l1
void union_find::unions(int l1, int l2) {
    // to simplify the procedure of insert
    if (l1==l2) return;
    // merge two set together
    vector<int>temp = leader[l2];
    for(auto it : temp)
        nodes[it] = l1;
    leader[l1].insert(leader[l1].begin(),leader[l2].begin(),leader[l2].end());
    leader.erase(l2);
}

// assuming the player0 plays vertically and player1 plays horizontally
// hence, player0's leader indicator is the # of row, and player1 is the # of column
bool union_find::insert(vector<int> n, vector<int> nbs, int player) {
    int index;
    // the "universal" rul mapping coordinates to node indices
    int n_val = n[0]*100+n[1];
    if (player==0) index = n[0];
    else index = n[1];
    vector<int> leaders;
    for (auto it: nbs) {
        int l = found(it);
        if (l!=-1)  leaders.push_back(l);
    }
    if (leaders.size()==0 || find(leaders.begin(),leaders.end(),index)==leaders.end()) {
        nodes[n_val] = index;
        leader[index] = vector<int>();
        leader[index].push_back(n_val);
        leaders.push_back(index);
    } else {
        nodes[n_val] = index;
        leader[index].push_back(n_val);
    }

    // rearrange nodes and leader in the map
    int new_leader = *min_element(leaders.begin(),leaders.end());
    int max_leader = *max_element(leaders.begin(),leaders.end());
    // keep the route connect to last
    if (new_leader==0 && max_leader==last) return true;
    if (max_leader==last)  new_leader = last;
    for (auto it: leaders)
        unions(new_leader, it);
    return false;
}

void union_find::print() {
    cout << "\nIn node map:" << endl;
    for (auto it: nodes)
        cout << "Node: " << it.first << "Leader: " << it.second << endl;
    cout << "\nIn leader map:" << endl;
    for (auto i: leader) {
        cout << "Leader: "<< i.first << endl;
        for (auto j: i.second)
            cout << j << "  ";
        cout << endl;
    }
}

