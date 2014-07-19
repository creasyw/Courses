"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1)==0 or len(list1)==1:
        return list1
    elif list1[0] == list1[1]:
        return remove_duplicates(list1[1:])
    else:
        return [list1[0]] + remove_duplicates(list1[1:])

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if len(list1)==0 or len(list2)==0:
        return []
    elif list1[0] < list2[0]:
        return intersect(list1[1:], list2)
    elif list1[0] > list2[0]:
        return intersect(list1, list2[1:])
    else:
        return [list1[0]] + intersect(list1[1:], list2[1:])

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    result = []
    while len(list1)!=0 and len(list2)!=0:
        if list1[0] <= list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    if len(list1) == 0:
        result += list2
    else:
        result += list1
    return result

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) == 1 or len(list1)==0:
        return list1
    else:
        return merge(merge_sort(list1[:len(list1)/2]), merge_sort(list1[len(list1)/2:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word)==1:
        return [word, ""]
    else:
        rest_strings = gen_all_strings(word[1:])
        this_round = []
        for item in rest_strings:
            for index in range(len(item)+1):
                this_round.append(item[0:index]+word[0]+item[index:])
        return this_round + rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
