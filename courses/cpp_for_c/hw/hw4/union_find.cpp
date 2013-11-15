#include <vector>
#include <iostream>
#include <unordered_map>
#include "union_find.h"

using namespace std;

// check if one node has already been explored
// if it is, return the leader element
int union_find::find(int i) {
    unordered_map<int, int>::iterator it = nodes.find(i);
    if (it == nodes.end())
        return -1;
    return it->second;
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
void union_find::insert(vector<int> n, vector<int> nbs, int player) {
    int index;
    // the "universal" rul mapping coordinates to node indices
    int n_val = n[0]*100+n[1];
    if (player==0)
        index = n[0];
    else
        index = n[1];
    vector<int> leaders;
    for (auto it: nbs) {
        int l = find(it);
        if (l!=-1)  leaders.push_back(l);
    }
    if (leaders.size()==0) {
        nodes[n_val] = index;
        leader[index] = vector<int>();
        leader[index].push_back(n_val);
    } else {
        int new_leader = *min_element(leaders.begin(), leaders.end());
        if (new_leader > index) {
            leader[index] = vector<int>();
            new_leader = index;
        }
        for (auto it: leaders)
            unions(new_leader, it);
        nodes[n_val] = new_leader;
        leader[new_leader].push_back(n_val);
    }
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

