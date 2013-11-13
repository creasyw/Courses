#include <iostream>
#include <vector>
#include <assert.h>
#include <cstring>

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
            string test(1, board[y][x*4]);
            string goal = ".";
            if(test!=goal) {
                cout << "The location has already been placed a move\n" <<
                "Please do another move."<< endl;
                return;
            } else if(player==0)
                board[y].replace(x*4, 1, "o");
            else
                board[y].replace(x*4, 1, "x");
        }

    private:
        int num;
        vector<string> board;
};


int main() {
    hex_game g(11);
    g.print_board();
    g.input_move(1, 0,0);
    g.input_move(1,9,7);
    g.print_board();
    g.input_move(0,9,7);
    g.print_board();
    return 0;
}

