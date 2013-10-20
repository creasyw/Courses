
#include <iostream>
using namespace std;

template <class T>
inline void myswap (T& i, T& j) {
  T temp = i;
  i = j;
  j = temp;
}

int main() {
  int m = 5, n = 10;
  double x = 5.3, y = 10.6;
  cout << "int input: "<<  m << ", " << n << endl;
  myswap(m,n);
  cout << "int output: "<<  m << ", " << n << endl;

  cout << "double input: "<<  x << ", " << y << endl;
  myswap(x,y);
  cout << "output: "<<  x << ", " << y << endl;
}

