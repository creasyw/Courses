#include <unordered_map>
#include <iostream>
#include <vector>
using namespace std;

/*
Run Status: Accepted!
Program Runtime: 8 milli secs
Progress: 10/10 test cases passed.

*/


vector<int> twoSum(vector<int> &numbers, int target) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function
    vector<int> result;
    unordered_map<int, int> mymap;
    int distance;
    for(int i=0; i!=numbers.size(); ++i)
    {
        distance = target- numbers[i];
        unordered_map<int, int>::const_iterator got = mymap.find (numbers[i]);
        if (got == mymap.end())
        {
            mymap.insert(std::make_pair(distance, i+1));
        }else{
            result.push_back(got->second);
            result.push_back(i+1);
            return result;
        }
    }
}



int main()
{
	int myints[] = {5, 75, 25};
	std::vector<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
	vector<int> path (twoSum(fifth, 100));
	for( vector<int>::const_iterator i=path.begin(); i!=path.end(); ++i)
    		std::cout << *i << std::endl;
}

