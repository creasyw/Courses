"""
Function to generate permutations of outcomes
Repetition of outcomes not allowed
"""


def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    assert length > 0, \
        "GEN_PERMUTATIONS -- It's nonsense to build permutation with length no larger than zero."
    assert len(outcomes) >= length, \
        "GEN_PERMUTATIONS -- The number of candidates should be no less than the length of permutation."

    def helper(items, num_picks):
        if num_picks == 1:
            return [(item, ) for item in items]
        result = []
        for item in items:
            temp = list(items)
            temp.remove(item)
            for tup in helper(temp, num_picks - 1):
                result.append((item, ) + tup)
        return result

    return set(helper(outcomes, length))


def run_example():

    # example for digits
    outcome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcome = ["Red", "Green", "Blue"]
    #outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    length = 2
    permtutations = gen_permutations(outcome, length)
    print "Computed", len(permtutations), "permutations of length", str(length)
    print "Permutations were", permtutations

#run_example()

#######################################
# Example output below
#
#Computed 90 permutations of length 2
#Permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])#
#
#Computed 6 permutations of length 2
#Permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green')])
#
## Final example for homework problem

outcome = set(["a", "b", "c", "d", "e", "f"])

permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print
print "Answer is", permutation_list[100]
