#ifndef MINHEAP_H
#define MINHEAP_H

#include "minheap.h"

// class for a node in heap
class heapitem {
    public:
        heapitem();
        heapitem(float k, int x);
        float get_key();
        void set_key(float k);
        int get_node();
        void set_node(int x);
    private:
        float key;
        int node;
};

// class for the operations of entire heap
class minheap {
    public:
        minheap(int n);
        void display();
        bool contains(int n);
        int size();
        heapitem pop();
        void update(float k, int n);
        void push(float k, int n);

    private:
        heapitem *elem;
        int num;            // the num of element
        int length;         // size of the array
        void heap_swap(heapitem &h1, heapitem &h2);
        int find(int n);
};

#endif
