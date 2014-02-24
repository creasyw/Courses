import numpy as np
from itertools import permutations

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

def reduce_dimension(m):
    """
    reduce the dimension of game matrix based on domination --
    player I will be better off if one row constently larger than another
    player II will be better off if one col constently smaller than anthoer
    Output: the reduced-size game matrix
    Note: This implements stric domination.
    TODO: convex reduction
    """
    local = np.array(m)
    flag = True
    while True:
        rbefore = len(local)
        candidates = []
        for nr in permutations(range(len(local)), 2):
            bigger = reduce(lambda x,y: x and y, local[nr[0]]>local[nr[1]])
            if bigger: 
                candidates.append(nr[1])
        for i in candidates:
            local = np.delete(local, i, 0)

        cbefore = len(local[0])
        candidates = []
        for nc in permutations(range(len(local[0])), 2):
            smaller = reduce(lambda x,y: x and y, local[:,nc[0]]<local[:, nc[1]])
            if smaller:
                candidates.append(nc[1])
        for i in candidates:
            local = np.delete(local, i, 1)

        if len(local[0])==cbefore and len(local)==rbefore:
            break

    return local
