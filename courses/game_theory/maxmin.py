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

import unittest
class BasicMatrixGame(unittest.TestCase):
    #def setUp(self):
        # m2 does not have N.E. point

    def test_nash_true(self):
        m1 = np.ones((5,3))
        m1[2][1] = 5
        self.assertTrue(nash_equilibrium(m1)==True)

    def test_nash_fail(self):
        m2 = np.array([[3,-1],[-1,9]])
        self.assertTrue(nash_equilibrium(m2)==False)

    def test_saddle_points(self):
        m2 = np.array([[3,-1],[-1,9]])
        self.assertEqual(saddle_points(m2), [(0,0),(1,0)])
    
    def test_reduce_dimension(self):
        m = np.array([[8,-1,-3,6],[-3,10,8,-4],[3,-4,-5,4]])
        self.assertTrue(np.array_equal(reduce_dimension(m),
                np.array([[-3,6],[8,-4]])))

suite = unittest.TestLoader().loadTestsFromTestCase(BasicMatrixGame)
unittest.TextTestRunner(verbosity=2).run(suite)

