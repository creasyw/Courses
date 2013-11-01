#include <iostream>

using namespace std;

// class for a node in heap
class heapitem {
    public:
        // initial func
        void heapitem(float k, int x) {
            key = k;
            node = x;
        }

        float get_key() {
            return key;
        }
        void set_key(float k) {
            key = k;
        }
        float get_node() {
            return node;
        }
        void set_node(int x) {
            node = x;
        }
    
    private:
        float key; // key is the up-to-date distance
        int node;
};

// class for the operations of entire heap
class minheap {
    public:
        void heap(int size) {
            elem = new heapitem[size];
            length = size;
        }

        // test if the heap contains certain element
        bool contains(float k) {
            for(int i=0; i<length; i++) {
                if (elem[i]==key) return true;
            }
            return false;
        }

        void heap_swap(const heapitem &h1, const heapitem &h2) {
            heapitem temp(0,0);
            temp.set_key(h1.get_key());
            temp.set_node(h1.get_node());
            h1.set_key(h2.get_key());
            h1.set_node(h2.get_node());
            h2.set_key(temp.get_key());
            h2.set_node(temp.set_node());
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

            heapitem result = elem[0];
            int current = 0;
            int child = 2;
            while (child<length) {
                if (elem[child-1].get_key() < elem[child].get_key()) {
                    heap_swap(elem[current], elem[child-1]);
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

        // update the key value of the element in the heap

        // push new element into the heap

                
    private:
        float *elem;
        int length;       // size of the array
};

