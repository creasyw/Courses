# Algorithm A (Addition of polynomials). This algorithm adds polynomial(P) to polynomial(Q),
# assuming that P and Q are pointer variables pointing to polynomials having the form above. The
# list P will be unchanged; the list Q will retain the sum. Pointer variables P and Q return to
# their starting points at the conclusion of this algorithm; auxiliary pointer variables Q1 and Q2
# are also used.
#
# A1. [Initialize.] Set P ← LINK(P), Q1 ← Q, Q ← LINK(Q). (Now both P and Q point to the leading
# terms of their polynomials. Throughout most of this algorithm the variable Q1 will be one step
# behind Q, in the sense that Q = LINK(Q1).)
# A2. [ABC(P):ABC(Q).] If ABC(P) < ABC(Q), set Q1 ← Q and Q ← LINK(Q) and repeat this step. If
# ABC(P) = ABC(Q), go to step A3. If ABC(P) > ABC(Q), go to step A5.
# A3. [Add coefficients.] (We’ve found terms with equal exponents.) If ABC(P) < 0, the algorithm
# terminates. Otherwise set COEF(Q) ← COEF(Q) + COEF(P). Now if COEF(Q) = 0, go to A4; otherwise,
# set P ← LINK(P), Q1 ← Q, Q ← LINK(Q), and go to A2. (Curiously the latter operations are identical
# to step A1.)
# A4. [Delete zero term.] Set Q2 ← Q, LINK(Q1) ← Q ← LINK(Q), and AVAIL ⇐ Q2. (A zero term created
# in step A3 has been removed from polynomial(Q).) Set P ← LINK(P) and go back to A2.
# A5. [Insert new term.] (Polynomial(P) contains a term that is not present in polynomial(Q), so we
# insert it in polynomial(Q).) Set Q2 ⇐ AVAIL, COEF(Q2) ← COEF(P), ABC(Q2) ← ABC(P), LINK(Q2) ← Q,
# LINK(Q1) ← Q2, Q1 ← Q2, P ← LINK(P), and return to step A2.
