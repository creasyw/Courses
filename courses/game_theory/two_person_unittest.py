import maxmin as mm
import unittest
import numpy as np

class BasicMatrixGame(unittest.TestCase):
    def setUp(self):
        self.m1 = np.ones((5,3))
        self.m1[2][1] = 5
        # m2 does not have N.E. point
        self.m2 = np.array([[3,-1],[-1,9]])

    def test_nash_true(self):
        self.assertTrue(mm.nash_equilibrium(self.m1)==True)

    def test_nash_fail(self):
        self.assertTrue(mm.nash_equilibrium(self.m2)==False)

    def test_saddle_points(self):
        self.assertEqual(mm.saddle_points(self.m2), [(0,0),(1,0)])

suite = unittest.TestLoader().loadTestsFromTestCase(BasicMatrixGame)
unittest.TextTestRunner(verbosity=2).run(suite)
