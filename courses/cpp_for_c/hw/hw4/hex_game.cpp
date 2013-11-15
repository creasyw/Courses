#include <iostream>
#include <vector>
#include <assert.h>
#include "union_find.h"

using namespace std;

class hex_game {
    public:
        inline hex_game(int n): num(n) {
            string dots = ".   ";
            string line;
            for(int i=0; i<num; ++i)
                line += dots;
            for(int i=0; i<num; ++i) {
                board.push_back(line);
            }
            uf[0] = new union_find(n);
            uf[1] = new union_find(n);
        }
        
        inline int transfer_coord (vector<int> n) {
            return n[0]*100+n[1];
        }

        void print_board() {
            string space = "  ";
            string spaces;
            for(int i=0; i<num; ++i) {
                cout<<spaces<<board[i]<<endl;
                spaces += space;
            }
            cout << endl;
        }
        void input_move(int player, int x, int y) {
            // sanity check for the input location
            assert (x>=0 && x<num && y>=0 && y<num);
            string test(1, board[x][y*4]);
            string goal = ".";
            if(test!=goal) {
                cout << "The location has already been placed a move\n" <<
                "Please do another move."<< endl;
                return;
            } else if (player==0) {
                put(x, y, 0);
                board[x].replace(y*4, 1, "o");
            }
            else {
                put(x, y, 1);
                board[x].replace(y*4, 1, "x");
            }
        }

// input the coordinate of move and return all its neighbors
        vector< vector<int> > neighbors(int x, int y) {
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

        void print_neighbors(vector<vector<int> > n) {
            cout << "The neighbors include:" << endl;
            for (auto it: n) {
                for (auto in: it)
                    cout << in << " ";
                cout << "\t";
            }
            cout << endl;
        }

        void put(int x, int y, int player) {
            vector<vector<int> > ns = neighbors(x, y);
            vector<int> ns_val;
            for (auto it: ns)
                ns_val.push_back(transfer_coord(it));
            vector<int> n;
            n.push_back(x);
            n.push_back(y);
            uf[player]->insert(n, ns_val, player);
            uf[player]->print();
        }


    private:
        int num;
        union_find* uf[2];
        vector<string> board;
};


int main() {
    hex_game g(11);
    g.print_board();
    g.input_move(1, 0,0);
    g.input_move(1,0,2);
    g.input_move(1,9,7);
    g.input_move(1,2,5);
    g.input_move(1,1,5);
    g.input_move(1,2,6);
    g.input_move(1,1,4);
    g.input_move(1,1,3);
    g.input_move(1,1,2);
    g.print_board();
    g.input_move(0,9,7);
    g.print_board();

    g.print_neighbors(g.neighbors(5,3));
    return 0;
}

