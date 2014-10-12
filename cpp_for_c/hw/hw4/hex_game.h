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
