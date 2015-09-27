"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1, provided.DRAW: 0, provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    result = board.check_win()
    if result == provided.DRAW:
        return 0, (-1, -1)
    elif result == provided.PLAYERX:
        return SCORES[provided.PLAYERX], (-1, -1)
    elif result == provided.PLAYERO:
        return SCORES[provided.PLAYERO], (-1, -1)

    # assign the worst case as initial value
    result = (-1, (-1, -1))
    # change player in the recursive calls
    another_player = provided.switch_player(player)
    # search best possible option among all subtrees
    for choice in board.get_empty_squares():
        local_board = board.clone()
        local_board.move(choice[0], choice[1], player)
        temp = mm_move(local_board, another_player)
        #print "Player:", player, "  Choice:", choice, "  Temp:", temp
        #print local_board
        # return once it has a best possible choice
        if temp[0] * SCORES[player] == 1:
            return temp[0], choice
        elif temp[0] * SCORES[player] > result[0]:
            result = (temp[0], choice)
        # update the choice of result if it keeps the worst
        elif result[0] == -1:
            result = (-1, choice)
    return result[0] * SCORES[player], result[1]


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    #print move
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

# for unit test
import poc_simpletest


def test_playerx():
    suite = poc_simpletest.TestSuite()
    print "Move PlayerX:"
    board = provided.TTTBoard(3, board=[[3, 2, 1], [3, 2, 1], [1, 3, 2]])
    print board
    suite.run_test(move_wrapper(board, provided.PLAYERX, 1), (2, 0), "Test 1.")
    suite.report_results()


def test_playero():
    suite = poc_simpletest.TestSuite()
    print "Move PlayerO:"
    board = provided.TTTBoard(3, board=[[3, 2, 1], [3, 2, 1], [2, 3, 2]])
    print board
    suite.run_test(move_wrapper(board, provided.PLAYERO, 1), (0, 2), "Test 2.")
    suite.report_results()


def owl_test():
    suite = poc_simpletest.TestSuite()
    board = provided.TTTBoard(3, board=[[2, 2, 3], [1, 2, 2], [3, 1, 3]])
    print board
    suite.run_test(move_wrapper(board, provided.PLAYERO, 1), (2, 1), "Test 3.")
    suite.report_results()

#test_playerx()
#test_playero()
#owl_test()
