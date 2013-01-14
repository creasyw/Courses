import numpy as np

class Node:
    def __init__ (self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert (root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print (root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print (root):
    if not root:
        return
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def max_depth (root):
    if not root:
        return 0
    return 1 + max(max_depth(root.l_child), max_depth(root.r_child))
def min_depth (root):
    if not root:
        return 0
    return 1+ min(min_depth(root.l_child), min_depth(root.r_child))
def is_balanced (root):
    return max_depth(root)-min_depth(root) <= 1


# for debug
def quick_build ():
    r = Node(3)
    binary_insert(r, Node(7))
    binary_insert(r, Node(1))
    binary_insert(r, Node(5))
    binary_insert(r, Node(4))
    return r

# Given a sorted (increasing order) array, write an algorithm 
# to create a binary tree with minimal height
def build_balanced_tree (root, arr):
    if len(arr) == 1:
        root = Node(arr[0])
        return root
    elif len(arr) == 0:
        return None
    mid = len(arr)/2
    root = Node(arr[mid])
    root.l_child = build_balanced_tree(root.l_child, arr[:mid])
    root.r_child = build_balanced_tree(root.r_child, arr[mid+1:])
    return root
def test_build_balanced_tree ():
    arr = np.arange(1,100)
    root = Node(0)
    root = build_balanced_tree(root, arr)
    print max_depth(root)
    print is_balanced(root)
    pre_order_print(root)

# Given a binary search tree, design an algorithm which creates a linked list of all the
# nodes at each depth (ie, if a tree has depth D, there should be D linked lists)
def level_linklist (root, arr, level):
    if root.l_child != None:
        arr[level+1].append(root.l_child.data)
        arr = level_linklist(root.l_child, arr, level+1)
    if root.r_child != None:
        arr[level+1].append(root.r_child.data)
        arr = level_linklist(root.r_child, arr, level+1)
    return arr
from collections import defaultdict
def test_level_linklist():
    arr = np.arange(1,100)
    root = Node(0)
    root = build_balanced_tree(root, arr)
    arr = defaultdict(list)
    arr[1] = [root.data]
    arr = level_linklist(root, arr, 1)
    print arr

# Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. NOTE: This is not necessarily a binary search tree.
# find_both = 0,1,2

# For depth-first search 1-visiting, 2-visited, and first visiting left than right child
def dfs (root, p, q, candidate, found):
    if root.data==p or root.data==q:
        candidate.append([root.data,1])
        return candidate, True
    candidate.append([root.data, 1])
    if root.l_child != None:
        candidate, found = dfs(root.l_child, p, q, candidate, found)
        if found:
            return candidate, found
    candidate[-1][1] = 2
    if root.r_child != None:
        candidate, found = dfs(root.r_child, p, q, candidate, found)
        if found:
            return candidate, found
    candidate.pop()
    return candidate, found
def test_dfs ():
    arr = np.arange(1,100)
    root = Node(0)
    root = build_balanced_tree(root, arr)
    result = dfs(root, 9, 31, [], False)
    print result


