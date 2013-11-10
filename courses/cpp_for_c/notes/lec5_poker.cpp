

enum class:short suit{SPADE, HEART, DIAMOND, CLUB};

class pips{
    public:
        pips(int val): v(val){assert(v>0 && v<14);}
        friend ostream& operator<<(ostream& out, pips p);
        inline int get_pips(){return v;}
    private:
        int v:
};

class card{
    public:
        card():s(suit::SPADE), v(1) {}
        card(suit s, pips v): s(s), v(v) {}
        friend ostream& operator<<(ostream& out, card c);
        suit get_suit() {return s;}
        pips get_pips() {return v;}
    private:
        suit s;
        pips v;
}




