#ifndef MINHEAP_H
#define MINHEAP_H

#include "minheap.h"

// class for a node in heap
class heapitem {
    public:
        heapitem();
        heapitem(float k, int x);
        inline float get_key() {return key;}
        inline int get_node() {return node;}
        inline void set_key(float k) {key = k;}
        inline void set_node(int x) {node = x;}
    private:
        float key;
        int node;
};

// class for the operations of entire heap
class minheap {
    public:
        minheap(int n);
        inline int size() {return num;}
        void display();
        bool contains(int n);
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
