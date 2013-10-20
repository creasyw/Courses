// homework-1: Convert C to C++

#include <iostream>
#include <vector>
const int N = 40;
using namespace std;

template <class T>
inline void sum(T& p, int n, vector<T> const& d)
{
  for (typename vector<T>::const_iterator it = d.begin(); it != d.end(); ++it)
     p += *it;
}

int main()
{
   vector<int> data;
   int accum = 0;
   for(int i = 0; i < N; ++i)
      data.push_back(i);

    sum(accum, N, data);
    cout << "sum is " << accum << endl;
    return 0;
}



