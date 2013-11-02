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
        minheap(int n) {
            elem = new heapitem[n];
            num = 0;
            length = n;
        }

        void display() {
            for (int i=0; i<num; ++i) {
                cout<< "Node: " << elem[i].get_node()
                << " with Key: " << elem[i].get_key() << endl;
            }
        }

        // test if the heap contains certain element
        bool contains(int n) {
            for(int i=0; i<num; i++) {
                if (elem[i].get_node()==n) return true;
            }
            return false;
        }

        // return the number of elements in the heap
        int size() {
            return num;
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
                if (elem[child-1].get_key() <= elem[child].get_key()) {
                    heap_swap(elem[current], elem[child-1]);
                    current = child-1;
                    child = child*2;
                } else {
                    swap(elem[current], elem[child]);
                    current = child;
                    child = (child+1)*2;
                }
            }
            if (current != num-1) {
                int parent = floor((current+1)/2.)-1;
                swap(elem[current], elem[num-1]);
                // the swapping breaks the heap property
                // the smaller node has to bubble-up
                if (elem[parent].get_key() > elem[current].get_key()) {
                    while (parent>=0 && elem[current].get_key()<elem[parent].get_key()) {
                        heap_swap(elem[current], elem[parent]);
                        current = parent;
                        parent = floor((current+1)/2.)-1;
                    }
                }
            }
            num -= 1;
            return result;
        }

        // update the key value of the element in the heap
        void update(float k, int n) {
            int current = find(n);
            if (current==-1)
                push(k, n);
            else if (elem[current].get_key() > k) {
                elem[current].set_key(k);
                int parent = floor((current+1)/2.)-1;
                // if the update breaks the heap property
                // the smaller node has to bubble-up
                if (elem[parent].get_key() > elem[current].get_key()) {
                    while (parent>=0 && elem[current].get_key()<elem[parent].get_key()) {
                        heap_swap(elem[current], elem[parent]);
                        current = parent;
                        parent = floor((current+1)/2.)-1;
                    }
                }
            }
        }

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

        void heap_swap(heapitem &h1, heapitem &h2) {
            heapitem temp(0,0);
            temp.set_key(h1.get_key());
            temp.set_node(h1.get_node());
            h1.set_key(h2.get_key());
            h1.set_node(h2.get_node());
            h2.set_key(temp.get_key());
            h2.set_node(temp.get_node());
        }

        // helper function for the update
        // find the index of the node, otherwise return -1
        int find(int n) {
            for(int i=0; i<num; i++) {
                if (elem[i].get_node()==n) return i;
            }
            return -1;
        }
};

int main() {
    minheap test(100);
    test.push(15, 2);
    test.push(9, 10);
    test.push(12, 7);
    test.push(11, 3);
    test.push(9, 15);
    test.push(4, 17);
    test.push(4, 12);
    test.push(8, 22);
    test.push(4, 21);

    test.display();

    // test for update heap
    cout << "change node 7 to 3" << endl;
    test.update(3, 7);
    test.display();

    // test for popping 5 times
    for (int i=0; i<5; ++ i) {
        cout << " " << endl;
        cout << "Test popping round " << i << endl;
        heapitem temp1 = test.pop();
        cout << "Popped up: " << temp1.get_node() << ": " << temp1.get_key() << endl;
        test.display();
    }

    return 0;
}

