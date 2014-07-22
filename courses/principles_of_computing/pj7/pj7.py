"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

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

    val = -1*SCORES[player]
    move = (-1, -1)
    if player == provided.PLAYERX:
        another_player = provided.PLAYERO
    else:
        another_player = provided.PLAYERX
    for choice in board.get_empty_squares():
        local_board = board.clone()
        local_board.move(choice[0], choice[1], player)
        temp = mm_move(local_board, another_player)*SCORES[player]
        if temp == 1:
            return 1*SCORES[player], choice
        elif temp > val:
            val = temp
            move = choice
    return val*SCORES[player], move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
