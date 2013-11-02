#include <iostream>
#include <math.h>

using namespace std;

// class for a node in heap
class heapitem {
    public:
        // initial func
        heapitem() {
            key = -1;
            node = -1;
        }
        heapitem(float k, int x) {
            key = k;
            node = x;
        }

        float get_key() {
            return key;
        }
        void set_key(float k) {
            key = k;
        }
        int get_node() {
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
        minheap(int size) {
            elem = new heapitem[size];
            num = 0;
            length = size;
        }

        void display() {
            for (int i=0; i<num; ++i) {
                cout<< "Node: " << elem[i].get_node()
                << " with Key: " << elem[i].get_key() << endl;
            }
        }

        // test if the heap contains certain element
        bool contains(float k) {
            for(int i=0; i<num; i++) {
                if (elem[i].get_key()==k) return true;
            }
            return false;
        }

        void heap_swap(heapitem &h1, heapitem &h2) {
            heapitem temp(0,0);
            temp.set_key(h1.get_key());
            temp.set_node(h1.get_node());
            h1.set_key(h2.get_key());
            h1.set_node(h2.get_node());
            h2.set_key(temp.get_key());
            h2.set_node(temp.get_node());
        }

        // main func: pop the minimum element out of the heap
        heapitem pop() {
            try {
                if (num==0)
                    throw length_error("There is no element in the heap!");
            }
            catch (const length_error& e) {
                cerr << "Heap Empty: " << e.what() << endl;
                exit (EXIT_FAILURE);
            }

            heapitem result(elem[0].get_key(), elem[0].get_node());
            int current = 0;
            int child = 2;
            // bubble-down for extraction
            while (child<num) {
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
            if (num%2==0)
                swap(elem[current], elem[num-1]);
            num -= 1;
            return result;
        }

        // update the key value of the element in the heap

        // push new element into the heap
        void push(float k, int n) {
            // if the heap is full, the element cannot be pushed in.
            try {
                if (num >= length)
                    throw length_error("There is no space in the heap!");
            }
            catch (const length_error& e) {
                cerr << "Heap Full: " << e.what() << endl;
                // no error comes out, but no operation performs
                return;
            }

            elem[num].set_key(k);
            elem[num].set_node(n);
            if (num!=0) {
                int current = num;
                int parent = floor((current+1)/2.)-1;
                // bubble-up for insertion
                while (parent >= 0) {
                    if (elem[current].get_key() > elem[parent].get_key())
                        break;
                    heap_swap(elem[current], elem[parent]);
                    current = parent;
                    parent = floor((current+1)/2.)-1;
                }
            }
            num += 1;
            return;
        }

    private:
        heapitem *elem;
        int num;            // the num of element
        int length;         // size of the array
};

int main() {
    minheap test(100);
    test.push(10.5, 2);
    test.push(3.14, 10);
    test.push(3.55, 7);

    test.display();
    return 0;
}

