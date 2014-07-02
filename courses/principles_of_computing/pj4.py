"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    result = [ 0 for _ in range(6)]
    for dice in hand:
        result[dice-1] += dice
    return max(result)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = [item+held_dice for item in gen_all_sequences(range(1, num_die_sides+1), num_free_dice)]
    scores = [score(hand) for hand in outcomes]
    return float(sum(scores))/len(scores)

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in range(r)[::-1]:
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    hand = tuple(sorted(hand))
    result = set([])
    for index in range(len(hand)):
        hold = hand[:index]
        comb = gen_all_sequences(hand[index:], len(hand[index:]))
        for item in comb:
            result.add(tuple(sorted(hold+item)))
    return result



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


#run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

# needs to be commented out for grading
import poc_simpletest

def test_score():
    suite = poc_simpletest.TestSuite()
    suite.run_test(score([1,2,3,4,5,6]), 6, "Test 0: Baisc functionality")
    suite.run_test(score([1,2,3,4,6,6]), 12, "Test 1: two are the same.")
    suite.run_test(score([1,1,1,1,1,5]), 5, "Test 2: two combinatories, same answer")

    suite.report_results()

def test_expected_value():
    suite = poc_simpletest.TestSuite()
    held_dice =  ()
    num_die_sides = 6
    num_free_dice = 2
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(5.0555556, 7), "Test #1:")


    held_dice =  (2, 1, 2)
    num_die_sides = 6
    num_free_dice = 3
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(6.9120370, 7), "Test #2:")


    held_dice =  (2,)
    num_die_sides = 6
    num_free_dice = 5
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(8.8801440, 7), "Test #3:")


    held_dice =  (1,)
    num_die_sides = 6
    num_free_dice = 2
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(5.0833333, 7), "Test #4:")


    held_dice =  (2, 1)
    num_die_sides = 6
    num_free_dice = 3
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(6.4722222, 7), "Test #5:")


    held_dice =  (2, 2)
    num_die_sides = 6
    num_free_dice = 5
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(9.2250514, 7), "Test #6:")


    held_dice =  (1, 2)
    num_die_sides = 6
    num_free_dice = 4
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(7.6689815, 7), "Test #7:")


    suite.report_results()
