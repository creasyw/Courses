#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;


class graph{
  public:
    // The graph is stored in a matrix
    graph(int n) {
        num = n;
        arr = new int*[num];
        for (int i=0; i<num; ++i)
            arr[i] = new int[num];
    }

    // return number of vertices
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

    // tests whether there is an edge from node x to node y.
    bool adjancent(int x, int y) {
        // sanity check for arguments
        try {
            if (x >= num || y >= num || x <0 || y < 0)
                throw invalid_argument("index of vertex is out of range");
        }
        catch (const invalid_argument& ia) {
            cerr << "Invalid argument: " << ia.what() << endl;
            exit (EXIT_FAILURE);
        }

        if (arr[x][y] > 0)
            return true;
        else
            return false;
    }
    
    // lists all nodes y such that there is an edge from x to y
    vector<int> neighbors(int x) {
        // sanity check for arguments
        try {
            if (x >= num || x <0)
                throw invalid_argument("index of vertex is out of range");
        }
        catch (const invalid_argument& ia) {
            cerr << "Invalid argument: " << ia.what() << endl;
            exit (EXIT_FAILURE);
        }

        vector<int> result;
        for (int i=0; i<num; ++i) {
            if (arr[x][i] > 0) result.push_back(i);
        }
        return result;
    }

    // adds to G the edge from x to y with value val, if it does not exist
    void add (int x, int y, int val) {
        // sanity check for arguments
        try {
            if (x >= num || y >= num || x <0 || y < 0)
                throw invalid_argument("index of vertex is out of range");
        }
        catch (const invalid_argument& ia) {
            cerr << "Invalid argument: " << ia.what() << endl;
            exit (EXIT_FAILURE);
        }

        if (arr[x][y] > 0 || x == y) return;
        arr[x][y] = arr[y][x] = val;
    }

    // removes the edge from x to y, if it is there
    void remove (int x, int y) {
        arr[x][y]=0;
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
            if (density > 1 || density <= 0 || lrange <=0 || urange < lrange)
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
        int**  arr;
    
};

int main()
{
    int n = 10;
    graph test(n);
    cout << "After initialization:" << endl;
    test.display_matrix();
    cout << "\nAfter generate:" << endl;
    test.undirected_matrix(0.5, 5, 10);
    test.display_matrix();
    cout << test.num_of_vertices() << endl;
    cout << test.num_of_edges() << endl;

    cout << "Test function neighbor(5): " << endl;
    vector<int> hit = test.neighbors(5);
    for( vector<int>::const_iterator i = hit.begin(); i != hit.end(); ++i)
            cout << *i << ' ';
    cout << "\n" << endl;

    cout << "Test add all edges connected node 2" << endl;
    for (int i=0; i<n; ++i) {
        test.add(2,i, 20);
    }
    test.display_matrix();

    cout << "Test delete all edges connected node 2" << endl;
    for (int i=0; i<n; ++i) {
        test.remove(2,i);
    }
    test.display_matrix();

}

