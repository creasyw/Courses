#include <iostream>

using namespace std;

// class for a node in heap
class heapitem {
    public:
        // initial func
        void heapitem(float k, int x, int y) {
            key = k;
            node1 = x;
            node2 = y;
        }

        float getter() {
            return key;
        }
        void setter(float k) {
            key = k;
        }
    
    private:
        float key; // key is the up-to-date distance
        int node1;
        int node2
};

// class for the operations of entire heap
class minheap {
    public:
        void heap(int size) {
            elem = new float[size];
            length = size;
        }

        // test if the heap contains certain element
        bool contains(int k) {
            for(int i=0; i<length; i++) {
                if (elem[i]==key) return true;
            }
            return false;
        }

        // main func: pop the minimum element out of the heap
        float pop() {
            try {
                if (length==0)
                    throw length_error("There is no element in the heap!");
            }
            catch (const length_error& e) {
                cerr << "Heap Empty" << e.what() << endl;
            }

            float result = elem[0];
            int current = 0;
            int child = 2;
            while (child<length) {
                if (elem[child-1] < elem[child]) {
                    swap(elem[current], elem[child-1]);
                    current = child-1;
                    child = (child-1)*2;
                } else {
                    swap(elem[current], elem[child]);
                    current = child;
                    child = child*2;
                }
            }
            if (length%2==0)
                swap(elem[current], elem[length-1]);
            length -= 1;
        }

                
    private:
        float *elem;
        int length;       // size of the array
};

