"""
Examples of invariants
"""

import math

# Invariants for loops


def iterative_factorial(num):
    """
    Iterative method for computing factorial
    """
    answer = 1
    index = 0
    assert answer == math.factorial(index)
    while index < num:
        index += 1
        answer *= index
        assert answer == math.factorial(index)
    # note that index == num so answer = math.factorial(num)
    return answer


def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in both list1 and list2.

    This function can be iterative.
    """
    answer = []
    assert answer == sorted(answer)

    idx1 = 0
    idx2 = 0
    while (idx1 < len(list1)) and (idx2 < len(list2)):
        if list1[idx1] < list2[idx2]:
            answer.append(list1[idx1])
            idx1 += 1
        elif list1[idx1] > list2[idx2]:
            answer.append(list2[idx2])
            idx2 += 1
        else:
            answer.append(list1[idx1])
            answer.append(list2[idx2])
            idx1 += 1
            idx2 += 1
        assert answer == sorted(answer)

    answer.extend(list1[idx1:])
    answer.extend(list2[idx2:])

    assert answer == sorted(answer)
    return answer

############################################
# Invariants for recursive functions


def recursive_factorial(num):
    """
    Recursive definition of factorial
    """
    if num == 0:
        answer = 1
        assert answer == math.factorial(num)
        return answer
    else:
        rec_part = recursive_factorial(num - 1)
        answer = num * rec_part
        assert answer == math.factorial(num)
        return answer


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        answer = list(list1)
        assert answer == sorted(answer)
        return answer

    mid = len(list1) // 2

    list_low = merge_sort(list1[0:mid])
    list_high = merge_sort(list1[mid:])

    answer = merge(list_low, list_high)
    assert answer == sorted(answer)
    return answer

########################################################
# Class invariant

import poc_grid
import poc_queue
import poc_wildfire_gui

# constants
EMPTY = 0
FULL = 1


class WildFire(poc_grid.Grid):
    """
    Class that models a burning wild fire using a grid and a queue
    The grid stores whether a cell is burned (FULL) or unburned (EMPTY)
    The queue stores the cells on the boundary of the fire
    """

    def __init__(self, grid_height, grid_width):
        """
        Override initializer for Grid, add queue to store boundary of fire
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        self._fire_boundary = poc_queue.Queue()

    def clear(self):
        """
        Set cells to be unburned and the fire boundary to be empty
        """
        poc_grid.Grid.clear(self)
        self._fire_boundary.clear()

    def enqueue_boundary(self, row, col):
        """
        Add cell with index (row, col) the boundary of the fire
        """
        self._fire_boundary.enqueue((row, col))

    def dequeue_boundary(self):
        """
        Remove an element from the boundary of the fire
        """
        return self._fire_boundary.dequeue()

    def boundary_size(self):
        """
        Return the size of the boundary of the fire
        """
        return len(self._fire_boundary)

    def fire_boundary(self):
        """
        Generator for the boundary of the fire
        """
        for cell in self._fire_boundary:
            yield cell
        # alternative syntax
        #return (cell for cell in self._fire_boundary)

    def update_boundary(self):
        """
        Function that spreads the wild fire using one step of BFS
        Updates both the cells and the fire_boundary
        """

        cell = self._fire_boundary.dequeue()
        neighbors = self.four_neighbors(cell[0], cell[1])
        #neighbors = self.eight_neighbors(cell[0], cell[1])
        for neighbor in neighbors:
            if self.is_empty(neighbor[0], neighbor[1]):
                self.set_full(neighbor[0], neighbor[1])
                self._fire_boundary.enqueue(neighbor)

        # Check class invariant after update
        assert self.boundary_invariant()

    def boundary_invariant(self):
        """
        Class invariant that checks whether every cell on the 
        boundary also has the corresponding grid cell set to FULL
        """
        for cell in self.fire_boundary():
            if self.is_empty(cell[0], cell[1]):
                print "Cell " + str(cell) + " in fire boundary is empty."
                return False
        return True


def run_examples():
    """
    Run several examples
    """
    print "iterative_factorial(4) is", iterative_factorial(4)

    print "merge([1, 3, 5, 8], [2, 4, 10]) is", merge([1, 3, 5, 8], [2, 4, 10])

    print "recursive_factorial(4) is", recursive_factorial(4)

    print "merge_sort([4, 2, 1, 4, 6, 7, 2, 1]) is", merge_sort([4, 2, 1, 4, 6,
                                                                 7, 2, 1])

    # run gui to visualize wildfire
    poc_wildfire_gui.run_gui(WildFire(30, 40))


run_examples()
