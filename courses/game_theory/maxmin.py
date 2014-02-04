import numpy as np

def nash_equilibrium(matrix):
    """ 
    input - matrix: np.ndarray
    output- has_ne: bool. whether the N.E. exists
    """
    # minimax of col == maximin of row
    return matrix.max(0).min()==matrix.min(1).max()
