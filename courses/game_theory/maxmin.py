import numpy as np

def nash_equilibrium(matrix):
    """ 
    input - matrix: np.ndarray
    output- has_ne: bool. whether the N.E. exists
    """
    # minimax of col == maximin of row
    return matrix.max(0).min()==matrix.min(1).max()

def saddle_points(matrix):
    """
    In the course, they are called (maximin, minimax) pair, but the essense is
    the same -- both players cannot achieve better results by deviating from them.
    input: extensive game in matrix form (ndarray)
    output: list of saddle points [(x1,y1),...,(xn, yn)]
    """
    mr = matrix.min(1)
    maximin = mr.max()
    mc = matrix.max(0)
    minimax = mc.min()
    return [(i, j) for i in range(len(mr)) if mr[i]==maximin \
                   for j in range(len(mc)) if mc[j]==minimax]
