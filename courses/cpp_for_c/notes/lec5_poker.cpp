#include<iostream>
#include<vector>
#include<algorithm>
#include<assert.h>

using namespace std;

enum class suit:short{SPADE, HEART, DIAMOND, CLUB};
ostream& operator<< (ostream& out, suit s) {
    cout << s;
    return out;
}

class pips{
    public:
        pips(int val): v(val){assert(v>0 && v<14);} // assert.h
        friend ostream& operator<<(ostream& out, pips p) {
            cout << p.v;
            return out;
        }
        inline int get_pips(){return v;}
    private:
        int v;
};

class card{
    public:
        card():s(suit::SPADE), v(1) {}
        card(suit s, pips v): s(s), v(v) {}
        friend ostream& operator<< (ostream& out, card c) {
            cout << c.v << c.s;
            return out;
        }
        suit get_suit() {return s;}
        pips get_pips() {return v;}
    private:
        suit s;
        pips v;
};



void init_deck(vector<card>& d) {
    for(int i=1; i<14; ++i) {
        card c(suit::SPADE, i);
        d[i-1] = c;
    }
    for(int i=1; i<14; ++i) {
        card c(suit::HEART, i);
        d[i+12] = c;
    }
    for(int i=1; i<14; ++i) {
        card c(suit::DIAMOND, i);
        d[i+25] = c;
    }
    for(int i=1; i<14; ++i) {
        card c(suit::CLUB, i);
        d[i+38] = c;
    }
}

void print(vector<card>& deck) {
    for(auto p: deck)
        cout << p;
    cout << endl;
}

bool is_flush(vector<card>& hand) {
    suit s = hand[0].get_suit();
    for (auto p: hand)
        if (s!= p.get_suit()) return false;
    return true;
}

int main() {
    vector<card> deck(52);
    srand(time(0));
    init_deck(deck);
    int how_many;
    int flush_count = 0;
    //int str_count = 0;
    //int str_flush_count = 0;
    cout << "How many shuffles?";
    cin >> how_many;

    for (int loop=0; loop<how_many; ++loop) {
        random_shuffle(deck.begin(), deck.end());
        vector<card> hand(5);
        int i = 0;
        for(auto p = deck.begin(); i<5; ++p)
            hand[i++] = *p;
        if (is_flush(hand))
            flush_count++;
    }
    cout << "Flushes "<<flush_count<<" out of "<<how_many<<endl;
}

