"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1    # Number of trials to run
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
    local_player = player    
    while len(empties)!=0:
        loc = empties.pop(random.randrange(len(empties)))
        board.move(loc[0], loc[1], player)
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
        raise ValueError("The board should have a final result! -- MC_UPDATE_SCORES")
    elif result == player:
        price = MCMATCH
        penalty = -MCOTHER
    else:
        price = -MCMATCH
        penalty = MCOTHER

    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if scores[row][col] == -1:
                continue
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
    maximum = 0
    for row in range(len(scores)):
        for col in range(len(scores[row])):
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
    scores = [[-1 for _ in range(ncol)] for _ in range(nrow)]
    for empty in empties:
        scores[empty[0]][empty[1]] = 0
    # begin trails
    for _ in range(trials):
        local_board = board.clone()
        mc_trial(local_board, player)
        mc_update_scores(scores, local_board, player)
        mv = get_best_move(board, scores)
        

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

