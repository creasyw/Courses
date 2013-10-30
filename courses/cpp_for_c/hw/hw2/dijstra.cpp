#include <iostream>
using namespace std;


class graph{
  public:
    graph(int n) {
        num = n;
    }

    void display_matrix(int nc, int nr, float (&array)[nc][nr]){
        for (int i=0; i <= nc; ++i){
	    for (int j=0; j <= nr; ++j)
		cout<< array[i][j] << " ";
	    cout << endl;
	}
    }

  private:
    int num;
    
};

int main()
{
    cout << "fuck c++" << endl;
}

