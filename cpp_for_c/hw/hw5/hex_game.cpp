#include <iostream>
#include <vector>
#include "union_find.h"
#include "hex_game.h"
#include <algorithm>    // for advance

using namespace std;

hex_game::hex_game(int n): num(n) {
    // hard coded as 1000 times of trails
    num_trails = 1000;
    string dots = ".   ";
    string line;
    for(int i=0; i<num; ++i) {
        line += dots;
        for (int j=0; j<num; j++)
            exmpty_slots[i*num+j] = 0;
    }
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

bool hex_game::input_move(int player, int x, int y) {
    string test(1, board[x][y*4]);
    string goal = ".";
    if(test!=goal) {
        cout << "The location has already been placed a move\n" <<
        "Please do another move."<< endl;
        return false;
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
    exmpty_slots.erase(exmpty_slots.find(x*num+y));
    return true;
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

vector<int> hex_game::random_select(unordered_map<int, int>& tempt) {
    vector<int> result;
    srand(clock());
    unordered_map<int, int>::const_iterator it(tempt.begin());
    advance(it, rand()%tempt.size());
    result.push_back(it->first / num);
    result.push_back(it->first - num*result[0]);
    return result;
}

vector<int> hex_game::best_move(int p) {
    int count = p;
    int player;
    temp[0](uf[0]);
    temp[1](uf[1]);
    unorder_map<int, int> score = exmpty_slots;

    for(int i=0; i<num_trails; ++i) {
        unorder_map<int, int> current = exmpty_slots;
        vector< vector<int> > moves;
        while (true) {
            player = count%2;
            ai_select = random_select(current);
            moves.push_back(ai_select);
        /*    if (ai_move(player, ai_select[0], ai_select[1])) {
                int x = moves[0][0];
                int y = moves[0][1];
                score[x*num+y]++;
                break;
            } else {
                count++;
            }*/
        }
    }

    int max_score = -1;
    int index = -1;
    for (auto it:score) {
        if (it->second > max_score) {
            max_score = it->second;
            index = it->first;
        }
    }
    vector<int> result;
    result.push_back(index/num);
    result.push_back(index-num*result[0]);
    return result;
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
    int x, y, player;
    int count = 0;
    vector<int> ai_select(2);
    string temp;
    bool p[2];
    // check if ai is needed
    cout << "AI acts as the first player [y,n]?" << endl;
    cin >> temp;
    if (temp=="y") p[0] = true;
    else p[0] = false;
    cout << "AI acts as the second player [y,n]?" << endl;
    cin >> temp;
    if (temp=="y") p[1] = true;
    else p[1] = false;
    
    // now, playing
    while (true) {
        player = count%2;
        cout << "Player "<< player << " input move: [0,"<<num-1<<"]"<< endl;
        if (p[player]) {
            ai_select = best_move(player);
            x = ai_select[0];
            y = ai_select[1];
        } else {
            while (true) {
                cout << "x = ";
                cin >> x;
                cout << "y = ";
                cin >> y;
                if (x>=0 && x<num && y>=0 && y<num) break;
                cout << "The input is out of range!" << endl;
            }
        }
        if (input_move(player, x, y)) {
            count++;
            // print board for every two legal moves
            if (player==1) print_board();
        }
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
        cout << "Please input the dimension of the board: ";
        cin >> i;
        if (i > 0) break;
        cout << "The dimension should be larger than zero!" << endl;
    }
    hex_game g(i);
    g.play();
    return 0;
}

