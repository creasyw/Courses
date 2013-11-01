#include <iostream>

using namespace std;

// class for a node in heap
class heapitem {
    public:
        // initial func
        void heapitem() {
            key = 0;
        }
        void heapitem(float k) {
            key = k;
        }

        float getter() {
            return key;
        }
        void setter(float k) {
            key = k;
        }
    
    private:
        float key;
};

// class for the operations of entire heap
class minheap {
    public:
        
    private:
        heapitem *elem;
        int num;        // num of elements in the heap
        int size;       // size of the array
};

