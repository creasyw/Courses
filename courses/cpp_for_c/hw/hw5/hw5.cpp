// ------------------- unionfind.h -------------------------//

#ifndef UNIONFIND_H
#define UNIONFIND_H

#include <unordered_map>
#include <vector>
#include "union_find.h"

using namespace std;

// data structure used in Kruskal's algorithm
class union_find {
    public:
        inline union_find(int n): last(n) {}
        inline int num_of_unions() {return leader.size();}
        int found(int i);
        void unions(int l1, int l2);
        bool insert(vector<int> n, vector<int> ns, int p);
        void print();
    private:
        int last;
        // the 1st element is the node, and the 2nd is the leader of cluster
        unordered_map<int, int > nodes;
        // the 1st element is the leader, and the 2nd are the nodes
        unordered_map<int, vector<int> > leader;
};

#endif


// ------------------- unionfind.cpp -------------------------//

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


// ------------------- hex_game.h -------------------------//
#ifndef HEX_GAME_H
#define HEX_GAME_H

#include <vector>
#include "union_find.h"

using namespace std;

class hex_game {
    public:
        hex_game(int n);
        // transfer coordinate into one number for storing in the map of union_find
        inline int transfer_coord (vector<int> n) {
            return n[0]*100+n[1];
        }
        // print the board with up-to-date moves
        void print_board();
        // maojor func for player to put a move on board
        void input_move(int player, int x, int y);
        // interact with union_find to store all moves
        bool put_check(int x, int y, int player);
        // input the coordinate of move and return all its neighbors
        vector< vector<int> > neighbors(int x, int y);
        // hepler function of neighbors
        void print_neighbors(vector<vector<int> > n);
        // major callee of the object to play the game
        void play();

    private:
        // the dimension of the board
        int num;
        // two union_find object for two players respectively
        union_find* uf[2];
        // used in print out the board
        vector<string> board;
};

#endif


// ------------------- hex_game.cpp -------------------------//
#include <iostream>
#include <vector>
#include "union_find.h"
#include "hex_game.h"

using namespace std;

hex_game::hex_game(int n): num(n) {
    string dots = ".   ";
    string line;
    for(int i=0; i<num; ++i)
        line += dots;
    for(int i=0; i<num; ++i) {
        board.push_back(line);
    }
    uf[0] = new union_find(n-1);
    uf[1] = new union_find(n-1);
}

void hex_game::print_board() {
    string space = "  ";
    string spaces;
    for(int i=0; i<num; ++i) {
        cout<<spaces<<board[i]<<endl;
        spaces += space;
    }
    cout << endl;
}
void hex_game::input_move(int player, int x, int y) {
    string test(1, board[x][y*4]);
    string goal = ".";
    if(test!=goal) {
        cout << "The location has already been placed a move\n" <<
        "Please do another move."<< endl;
        return;
    } else if (player==0) {
        board[x].replace(y*4, 1, "X");
        if (put_check(x, y, 0)) {
            cout << "The player 0 is the winner!" << endl;
            print_board();
            exit(0);
        }
    }
    else {
        board[x].replace(y*4, 1, "O");
        if (put_check(x, y, 1)) {
            cout << "The player 1 is the winner!" << endl;
            print_board();
            exit(0);
        }
    }
}

bool hex_game::put_check(int x, int y, int player) {
    vector<vector<int> > ns = neighbors(x, y);
    vector<int> ns_val;
    for (auto it: ns)
        ns_val.push_back(transfer_coord(it));
    vector<int> n;
    n.push_back(x);
    n.push_back(y);
    return uf[player]->insert(n, ns_val, player);
}


vector< vector<int> > hex_game::neighbors(int x, int y) {
    vector< vector<int> > result;
    vector<int> temp;
    if (y+1<num) {
        temp.push_back(x);
        temp.push_back(y+1);
        result.push_back(temp);
        temp.clear();
    }
    if (y-1>=0) {
        temp.push_back(x);
        temp.push_back(y-1);
        result.push_back(temp);
        temp.clear();
    }
    if (x-1 >=0) {
        temp.push_back(x-1);
        temp.push_back(y);
        result.push_back(temp);
        temp.clear();
        if (y+1<num) {
            temp.push_back(x-1);
            temp.push_back(y+1);
            result.push_back(temp);
            temp.clear();
        }
    }
    if (x+1 < num) {
        temp.push_back(x+1);
        temp.push_back(y);
        result.push_back(temp);
        temp.clear();
        if (y-1>=0) {
            temp.push_back(x+1);
            temp.push_back(y-1);
            result.push_back(temp);
        }
    }
    return result;
}

void hex_game::print_neighbors(vector<vector<int> > n) {
    cout << "The neighbors include:" << endl;
    for (auto it: n) {
        for (auto in: it)
            cout << in << " ";
        cout << "\t";
    }
    cout << endl;
}

void hex_game::play() {
    int x, y;
    while (true) {
        cout << "Player 0 input move: [0,"<<num-1<<"]"<< endl;
        while (true) {
            cout << "x = ";
            cin >> x;
            cout << "y = ";
            cin >> y;
            if (x>=0 && x<num && y>=0 && y<num) break;
            cout << "The input is out of range!" << endl;
        }
        input_move(0, x, y);
        cout << "Player 1 input move: [0,"<<num-1<<"]"<< endl;
        while (true) {
            cout << "x = ";
            cin >> x;
            cout << "y = ";
            cin >> y;
            if (x>=0 && x<num && y>=0 && y<num) break;
            cout << "The input is out of range!" << endl;
        }
        input_move(1, x, y);
        print_board();
    }
}


void test() {
    hex_game g(11);
    g.print_board();
    g.input_move(1,8,9);
    g.input_move(1,0,2);
    g.input_move(1,9,7);
    g.input_move(1,9,6);
    g.input_move(1,9,5);
    g.input_move(1,9,4);
    g.input_move(1,9,3);
    g.input_move(1,9,2);
    g.input_move(1,9,0);
    g.input_move(1,9,1);
    g.input_move(1,8,8);
    g.input_move(1,9,10);
    g.input_move(1,9,9);
    g.input_move(1,1,4);
    g.input_move(1,1,3);
    g.input_move(1,1,2);

    g.print_neighbors(g.neighbors(5,3));
}


// ------------------- main function -------------------------//
int main() {
    int i;
    while (true) {
        cout << "Please input the dimension of the board (7 or 11): ";
        cin >> i;
        if (i==7 || i==11) break;
        cout << "The dimension should be 7 or 11!" << endl;
    }
    hex_game g(i);
    g.play();
    return 0;
}


