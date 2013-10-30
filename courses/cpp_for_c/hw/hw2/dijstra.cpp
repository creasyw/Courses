#include <iostream>
#include <stdlib.h>

using namespace std;


class graph{
  public:
    graph(int n) {
        num = n;
        arr = new float*[num];
        for (int i=0; i<num; ++i)
            arr[i] = new float[num];
    }

    void display_matrix(){
        for (int i=0; i < num; ++i) {
            for (int j=0; j < num; ++j)
            cout<< arr[i][j] << " ";
            cout << endl;
        }
    }

    void generate_matrix(float density, int lrange, int urange) {
        int num_of_edges = static_cast<int>(num*num*density);
        int count = 0;
        cout << num_of_edges << endl;
        while (count < num_of_edges) {
            srand(clock());
            int col = rand() % num;
            int row = rand() % num;
            // if the route has been set, it doesn't need to set again.
            // Or, there is no sense to set diagonal elements
            if (arr[row][col] > 0 || row == col)
                continue;
            int val = rand() % (urange - lrange + 1) + lrange;
            arr[row][col] = val;
            count++;
        }
    }

  private:
      int num;
      float**  arr;
    
};

int main()
{
    cout << "fuck c++" << endl;
    graph test(10);
    cout << "After initialization:" << endl;
    test.display_matrix();
    cout << "\nAfter generate:" << endl;
    test.generate_matrix(0.1, 5, 10);
    test.display_matrix();

}

