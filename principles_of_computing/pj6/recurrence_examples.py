"""
Examples of recursive functions and recurrences derived
from those functions
"""

# First example with binary numbers of a given length


def make_binary(length):
    """
    Function that generates an ordered list of binary numbers in 
    ascending order
    """
    if length == 0:
        return [""]

    all_but_first = make_binary(length - 1)

    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)
    for bits in all_but_first:
        answer.append("1" + bits)
    return answer


def run_bin_example(num):
    """
    print out example of binary representations
    """
    print
    print "Binary numbers of length", num
    print make_binary(num)


run_bin_example(4)


def binary_length(length):
    """
    Recurrence for the number of binary numbers 
    of a given length
    """

    if length == 0:
        return 1
    else:
        return 2 * binary_length(length - 1)

#for length in range(10):
#    print binary_length(length)

# Second example for running time of binary search


def binary_search(ordered_list, item):
    """
    Recursively check whether an item lies in non-empty ordered_list
    """

    if len(ordered_list) == 1:
        return item == ordered_list[0]
    mid = len(ordered_list) / 2
    if item < ordered_list[mid]:
        return rec1_binary_search(ordered_list[:mid], item)
    else:
        return rec1_binary_search(ordered_list[mid:], item)


def search_time(length):
    """
    Recurrence that estimates the running time of
    binary search of a sorted list of given length
    """
    if length == 1:
        return 1
    else:
        return 1 + search_time(length / 2)

#for value in range(10):
#    print "Searching a sorted list of length", 2 ** value, "in time", \
#           search_time(2 ** value)
