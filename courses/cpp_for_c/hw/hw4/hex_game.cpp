#include <iostream>
#include <vector>

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
        }
    private:
        int num;
        vector<string> board;
};


int main() {
    hex_game g(11);
    g.print_board();
    return 0;
}

