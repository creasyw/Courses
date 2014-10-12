#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void getw(string& t, ifstream& in) {
    in >> t;
}

int read_string(vector<string> &words, ifstream& in) {
    int i = 0;
    while (!in.eof())
        getw(words[i++], in);
    return (i-1);
}

int main() {
    vector<string> w(1000);
    ifstream ifp("data");
    int howmany = read_string (w, ifp); //lec12

    w.resize(howmany);
    sort(w.begin(), w.end());
    for(auto str: w)
        cout << str << "\t";
}


