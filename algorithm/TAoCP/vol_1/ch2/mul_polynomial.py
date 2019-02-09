# Algorithm M (Multiplication of polynomials). This algorithm, analogous to Algorithm A, replaces
# polynomial(Q) by
#     polynomial(Q) + polynomial(M) × polynomial(P).
#
# M1. [Next multiplier.] Set M ← LINK(M). If ABC(M) < 0, the algorithm terminates.
# M2. [Multiply cycle.] Perform Algorithm A, except that wherever the notation “ABC(P)” appears in
# that algorithm, replace it by “(if ABC(P) < 0 then −1, otherwise ABC(P) + ABC(M))”; wherever
# “COEF(P)” appears in that algorithm replace it by “COEF(P) × COEF(M)”. Then go back to step M1.
