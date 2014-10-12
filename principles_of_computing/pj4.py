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
    max_dice = max(hand)
    result = [ 0 for _ in range(max_dice)]
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

def combinations(iterable, leng):
    """
    implement combinations for 'iterable' with given length
    """
    pool = tuple(iterable)
    maxi = len(pool)
    if leng > maxi:
        return
    indices = range(leng)
    yield tuple(pool[index] for index in indices)
    while True:
        counter = 0
        for index in range(leng)[::-1]:
            if indices[index] != index + maxi - leng:
                counter = index
                break
        else:
            return
        indices[counter] += 1
        for index_1 in range(counter+1, leng):
            indices[index_1] = indices[index_1-1] + 1
        yield tuple(pool[index] for index in indices)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result = set([()])
    # the number of cards left
    for length in range(1, len(hand)+1):
        # all possible combinations given the length
        for item in combinations(hand, length):
            result.add(item)
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
    hold = tuple()
    expect_value = 0.0
    for choice in gen_all_holds(hand):
        value = expected_value(choice, num_die_sides, len(hand)-len(choice))
        if value > expect_value:
            expect_value = value
            hold = choice
    return (expect_value, hold)

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
