import maxmin as mm
import unittest
import numpy as np

class BasicMatrixGame(unittest.TestCase):
    def test_cases(self):
        self.m1 = np.ones((5,3))
        self.m1[2][1] = 5

    def nash_test(self):
        self.assertTrue(nash_equilibrium(self.m1)==True)

suite = unittest.TestLoader().loadTestsFromTestCase(BasicMatrixGame)
unittest.TextTestRunner(verbosity=2).run(suite)
