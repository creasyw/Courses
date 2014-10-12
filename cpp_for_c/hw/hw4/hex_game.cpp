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

