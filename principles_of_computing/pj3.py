"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    It plays a game starting with the given player by making random moves,
    alternating between players, and returning when the game is over.
    The modified board will contain the state of the game, so the function
    does not return anything.
    """
    empties = board.get_empty_squares()
    random.shuffle(empties)
    local_player = player
    while len(empties) != 0:
        loc = empties.pop()
        board.move(loc[0], loc[1], local_player)
        if board.check_win() is not None:
            break
        local_player = provided.switch_player(local_player)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe board, a board from a completed game,
    and which player the machine player is.
    It scores the completed board and update the scores grid. 
    As the function updates the scores grid directly, it does not return anything.
    """
    result = board.check_win()
    if result == provided.DRAW:
        return
    price = penalty = 0
    if result is None:
        raise ValueError(
            "The board should have a final result! -- MC_UPDATE_SCORES")
    elif result == player:
        price = MCMATCH
        penalty = -MCOTHER
    else:
        price = -MCMATCH
        penalty = MCOTHER

    for row in range(len(scores)):
        for col in range(len(scores[row])):
            status = board.square(row, col)
            if status == player:
                scores[row][col] += price
            # add score for the other player, if that slot is not empty
            elif status != provided.EMPTY:
                scores[row][col] += penalty


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    It finds all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple.
    """
    candidates = []
    maximum = float('-inf')
    empties = board.get_empty_squares()
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if (row, col) not in empties:
                continue
            if scores[row][col] > maximum:
                maximum = scores[row][col]
                candidates = [(row, col)]
            elif scores[row][col] == maximum:
                candidates.append((row, col))
    return candidates[random.randrange(len(candidates))]


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. It uses the Monte Carlo simulation
    described above to return a move for the machine player in the form of a
    (row, column) tuple. Be sure to use the other functions you have written!
    """
    # make sure the updating score is for empty slots
    # the representation of "scores" is dictated by the API
    empties = board.get_empty_squares()
    if len(empties) == 0:
        raise AssertionError("The board is full! -- MC_MOVE")
    nrow = ncol = board.get_dim()
    scores = [[0 for _ in range(ncol)] for _ in range(nrow)]
    # begin trails
    for _ in range(trials):
        local_board = board.clone()
        mc_trial(local_board, player)
        mc_update_scores(scores, local_board, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

# needs to be commented out for grading
import poc_simpletest


def test_trial(mc_trial):
    """ Test for mc_trial() """

    print "Testing the mc_trial function."

    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()

    my_board = provided.TTTBoard(3)
    mc_trial(my_board, provided.PLAYERO)
    suite.run_test(my_board.check_win() is not None, True,
                   "Test 1: mc_trial completes 3x3 game")

    my_board = provided.TTTBoard(4)
    mc_trial(my_board, provided.PLAYERO)
    suite.run_test(my_board.check_win() is not None, True,
                   "Test 2: mc_trial completes 4x4 game")

    suite.report_results()


def manual_scoring(mc_update_scores, mcmatch, mcother, scores, player,
                   arrangement):
    """ Perform one trial of scoring """

    my_board = provided.TTTBoard(3, board=arrangement)
    mc_update_scores(scores, my_board, player)

    print my_board
    print "Player =", provided.STRMAP[player], scores


def test_update_scores(mc_update_scores, mcmatch, mcother):
    """ Test for mc_update_scores() """

    print "Testing the mc_update_scores function with a sequence of scoring."
    print "Try setting different MCMATCH/MCOTHER values for this test."
    print "MCMATCH:", mcmatch
    print "MCOTHER:", mcother
    print

    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()
    scores = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

    manual_scoring(mc_update_scores, mcmatch, mcother, scores,
                   provided.PLAYERX, [[2, 1, 3], [3, 2, 1], [2, 3, 2]])
    suite.run_test(scores, [[mcmatch, 0.0, -mcother], [-mcother, mcmatch, 0.0],
                            [mcmatch, -mcother, mcmatch]],
                   "Test 1: X won, player is X")

    manual_scoring(mc_update_scores, mcmatch, mcother, scores,
                   provided.PLAYERO, [[2, 1, 3], [3, 2, 1], [2, 3, 2]])
    suite.run_test(scores, [[mcmatch + mcother, 0.0, -mcother - mcmatch
                             ], [-mcother - mcmatch, mcmatch + mcother, 0.0],
                            [mcmatch + mcother, -mcother - mcmatch,
                             mcmatch + mcother]],
                   "Test 2: Same game, X won, player is O")

    manual_scoring(mc_update_scores, mcmatch, mcother, scores,
                   provided.PLAYERX, [[2, 3, 2], [3, 3, 2], [3, 2, 3]])
    suite.run_test(scores, [[mcmatch + mcother, 0.0, -mcother - mcmatch
                             ], [-mcother - mcmatch, mcmatch + mcother, 0.0],
                            [mcmatch + mcother, -mcother - mcmatch,
                             mcmatch + mcother]], "Test 3: Tied game")

    manual_scoring(mc_update_scores, mcmatch, mcother, scores,
                   provided.PLAYERX, [[1, 3, 2], [2, 3, 1], [1, 3, 2]])
    suite.run_test(scores, [[mcmatch + mcother, mcother, -mcother - 2 * mcmatch
                             ], [-mcother - 2 * mcmatch, mcmatch + 2 * mcother,
                                 0.0], [mcmatch + mcother, -mcmatch, mcother]],
                   "Test 4: O won, player is X")

    manual_scoring(mc_update_scores, mcmatch, mcother, scores,
                   provided.PLAYERO, [[1, 2, 2], [3, 3, 3], [3, 2, 2]])
    suite.run_test(scores, [[mcmatch + mcother, 0.0, -2 * mcother - 2 * mcmatch
                             ], [-mcother - mcmatch, 2 * mcmatch + 2 * mcother,
                                 mcmatch], [2 * mcmatch + mcother,
                                            -mcmatch - mcother, 0.0]],
                   "Test 5: O won, player is O")

    suite.report_results()


def test_best_move(get_best_move):
    """ Test for get_best_move() """

    print "Testing the get_best_move function."

    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()

    my_board = provided.TTTBoard(3, board=[[2, 3, 2], [1, 1, 1], [1, 2, 3]])
    scores = [[3.0, 5.0, -1.0], [3.0, 2.0, -8.0], [4.0, -2.0, 2.0]]

    print my_board
    print "scores:", scores
    suite.run_test(
        get_best_move(my_board, scores), (2, 0), "Test 1: Best move")

    my_board = provided.TTTBoard(3, board=[[1, 1, 2], [1, 3, 1], [2, 3, 1]])
    scores = [[0.0, 2.0, 1.0], [0.0, 2.0, -1.0], [1.0, -2.0, 2.0]]
    move_set = set([])
    for dummy_idx in range(20):
        move_set.add(get_best_move(my_board, scores))

    print my_board
    print "scores:", scores
    suite.run_test(move_set, set([(0, 1), (2, 2)]),
                   "Test 2: Two possible best moves")

    suite.report_results()


test_trial(mc_trial)
test_update_scores(mc_update_scores, MCMATCH, MCOTHER)
test_best_move(get_best_move)
