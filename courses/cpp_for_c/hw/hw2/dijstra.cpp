#include <iostream>
#include <stdlib.h>

using namespace std;


class graph{
  public:
    // The graph is stored in a matrix
    graph(int n) {
        num = n;
        arr = new float*[num];
        for (int i=0; i<num; ++i)
            arr[i] = new float[num];
    }

    int num_of_vertices() {
        return num;
    }

    // This is specific for the undirected graph
    int num_of_edges() {
        int count = 0;
        for (int i=0; i < num-1; ++i)
            for (int j = i+1; j < num; ++j)
                if (arr[i][j] > 0) count++;
        return count;
    }

    void display_matrix(){
        for (int i=0; i < num; ++i) {
            for (int j=0; j < num; ++j)
            cout<< arr[i][j] << " ";
            cout << endl;
        }
    }

    void directed_matrix(float density, int lrange, int urange) {
        // sanity check for arguments
        try {
            if (density > 1 || density <= 0 || lrange <=0 or urange < lrange)
                throw invalid_argument("Density should be in (0,1] and 0 < lrange < urange");
        }
        catch (const invalid_argument& ia) {
            cerr << "Invalid argument: " << ia.what() << endl;
            return;
        }

        int nedge = static_cast<int>(num*(num-1)*density);
        int count = 0;
        cout << nedge << endl;
        while (count < nedge) {
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
    
    // The undirected matrix has the same value for both [i,j] and [j,i]
    void undirected_matrix(float density, int lrange, int urange) {
        // sanity check for arguments
        try {
            if (density > 1 || density <= 0 || lrange <=0 or urange < lrange)
                throw invalid_argument("Density should be in (0,1] and 0 < lrange < urange");
        }
        catch (const invalid_argument& ia) {
            cerr << "Invalid argument: " << ia.what() << endl;
            return;
        }

        int nedge = static_cast<int>(num*(num-1)/2*density);
        cout << num*(num-1)/2 << endl;
        cout << nedge << endl;
        int count = 0;
        while (count < nedge) {
            srand(clock());
            int row = rand() % num;
            int col = rand() % (num-row);
            // if the route has been set, it doesn't need to set again.
            // Or, there is no sense to set diagonal elements
            if (arr[row][col] > 0 || row == col)
                continue;
            int val = rand() % (urange - lrange + 1) + lrange;
            arr[row][col] = arr[col][row] = val;
            count++;
        }
    }

    private:
        int num;
        float**  arr;
    
};

int main()
{
    graph test(10);
    cout << "After initialization:" << endl;
    test.display_matrix();
    cout << "\nAfter generate:" << endl;
    test.undirected_matrix(0.5, 5, 10);
    test.display_matrix();
    cout << test.num_of_vertices() << endl;
    cout << test.num_of_edges() << endl;

}

