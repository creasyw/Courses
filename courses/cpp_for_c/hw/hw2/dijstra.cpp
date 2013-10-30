#include <iostream>

class graph{
  public:
    graph(int n) num = n;

    void display_matrix(const float& m, int nr, int nc){
      for (int i=0; i <= nr; ++i){
	  for (int j=0; j <= nc; ++j)
	    cout<< m[i][j] << " ";
	  cout << endl;
      }
    }

  private:
    int num;
    
}



