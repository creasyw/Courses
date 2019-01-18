# Algorithm I (Inverse in place). Replace X[1]X[2] ... X[n], a permutation of {1, 2, ..., n}, by its
# inverse. This algorithm is due to Bing-Chao Huang [Inf. Proc. Letters 12 (1981), 237–238].
#
# I1. [Initialize.] Set m ← n, j ← −1.
# I2. [Next element.] Set i ← X[m]. If i < 0, go to step I5 (the element has already been
# processed).
# I3. [Invert one.] (At this point j < 0 and i = X[m]. If m is not the largest element of its cycle,
# the original permutation had X [−j] = m.) Set X[m] ← j, j ← −m, m ← i, i ← X[m].
# I4. [End of cycle?] If i > 0, go back to I3 (the cycle has not ended); otherwise set i ← j. (In
# the latter case, the original permutation had X [−j] = m, and m is largest in its cycle.)
# I5. [Store final value.] Set X[m] ← −i. (Originally X [−i] was equal to m.)
# I6. [Loop on m.] Decrease m by 1. If m > 0, go back to I2; otherwise the algorithm terminates.
