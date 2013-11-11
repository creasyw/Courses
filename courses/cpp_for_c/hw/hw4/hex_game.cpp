#include<iostream>

using namespace std;

class hex_game {
    public:
        inline hex_game(int n): num(n) {}
        void print_board() {
            string space = "  ";
            string dots = ".   ";
            string line, spaces;
            for(int i=0; i<num; ++i)
                line += dots;
            for(int i=0; i<num; ++i) {
                cout<<spaces<<line<<endl;
                spaces += space;
            }
        }
    private:
        int num;
};


int main() {
    hex_game g(11);
    g.print_board();
    return 0;
}

