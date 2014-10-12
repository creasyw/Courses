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

def binary_search (root, val, route):
    """
    Find specific element in BST and return the route for that element
    For the convenience of successive function, the route contains the node rather
    than only values of them.
    """
    if root is None:
        # print "The value %s is not stored in the tree"%(val)
        return []
    else:
        route.append(root)
        # root.data==val, then do nothing about recursion
        if root.data > val:
            route = binary_search(root.l_child, val, route)
        elif root.data < val:
            route = binary_search(root.r_child, val, route)
    return route

def binary_minimum (root):
    while root.l_child is not None:
        root = root.l_child
    return root.data
def binary_successor (root, val):
    route = binary_search(root, val, [])
    if len(route) != 0:
        x = route.pop()
        if x.r_child is not None:
            return binary_minimum(x.r_child)
        while len(route)!=0:
            y = route.pop()
            if x == y.l_child:
                return y.data
            else:
                x = y
    print "There is no successor for the given element."
    return

def replace_node (parent, target, replacement):
    if parent.l_child == target:
        parent.l_child = replacment
    else:
        parent.r_child = replacement

def binary_delete (root, val):
    route = binary_search(root, val, [])
    if len(route)!=0:
        z = route.pop()     # The deleted node
        y = route.pop()
        # z has no children
        if z.l_child is None and z.r_child is None:
            replace_node(y, z, None)
        # z only has left child
        elif z.r_child is None:
            replace_node(y, z, z.l_child)
        # z has right child
        else:
            x = binary_successor(z, z.data)
            subroute = binary_search(z, x, [])
            x = subroute.pop()
            if len(subroute) == 0:
                replace_node(y, z, x)
            else:
                x_p = subroute.pop()
                # Because x is the successor of z, x is "left-most" node in the subtree
                x_p.l_child = x.r_child
                replace_node(y, z, x)
    return root

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
    arr = np.arange(1,100)
    root = Node(0)
    return build_balanced_tree(root, arr)

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
def test_level_linklist(root):
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



