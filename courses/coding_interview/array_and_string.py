# 1.1 Implement an algorithm to determine if a string has all unique 
# characters What if you can not use additional data structures?
def is_unique (s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

# Write code to reverse a C-Style String 
def reverse_wholestring (s):
    return s[::-1]

def reverse_wordorder (s):
    return ' '.join(s.split()[::-1])

# Design an algorithm and write code to remove the duplicate characters
# in a string without using any additional buffer 
# NOTE: One or two additional variables are fine An extra copy of the array is not
def remove_duplicate (s):
    result = set()
    for i in s:
        result.add(i)
    return ''.join(result)

# Write a method to decide if two strings are anagrams or not
def is_anagram (s, t):
    if sorted(s) == sorted(t):
        return True
    return False 

# Write a method to replace all spaces in a string with ‘%20’
import re
def replace_space (s):
    return re.subn(' ', '%20', s)[0]

# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column is set to 0
import numpy as np
def set_zero (m):
    nrow = len(m)
    ncol = len(m[0])
    col_flag = np.ones(ncol)
    row_flag = False
    for i in range(nrow):
        for j in range(ncol):
            if m[i][j] == 0:
                row_flag = True
                col_flag[j] = 0
        if row_flag:
            m[i] = np.zeros(ncol)
            row_flag = False
    for j in range(ncol):
        if col_flag[j] == 0:
            m[:,j] = np.zeros(nrow)
    return m

