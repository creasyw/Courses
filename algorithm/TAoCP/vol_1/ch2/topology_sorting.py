# Algorithm T (Topological sort). This algorithm inputs a sequence of relations j ≺ k, indicating
# that object j precedes object k in a certain partial ordering, assuming that 1 ≤ j, k ≤ n. The
# output is the set of n objects embedded in a linear order. The internal tables used are: QLINK[0],
# COUNT[1] = QLINK[1], COUNT[2] = QLINK[2], . . ., COUNT[n] = QLINK[n]; TOP[1], TOP[2], . . .,
# TOP[n]; a storage pool with one node for each input relation and with SUC and NEXT fields as shown
# above; P, a Link variable used to refer to the nodes in the storage pool; F and R, integer-valued
# variables used to refer to the front and rear of a queue whose links are in the QLINK table; and
# N, a variable that counts how many objects have yet to be output.
#
# T1. [Initialize.] Input the value of n. Set COUNT[k] ← 0 and TOP[k] ← Λ for 1 ≤ k ≤ n. Set N ← n.
# T2. [Next relation.] Get the next relation “j ≺ k” from the input; if the input has been
# exhausted, however, go to T4.
# T3. [Record the relation.] Increase COUNT[k] by one. Set
#     P ⇐ AVAIL, SUC(P) ← k, NEXT(P) ← TOP[j], TOP[j] ← P.
# (This is operation (8).) Go back to T2.
# T4. [Scan for zeros.] (At this point we have completed the input phase; the input (18) would now
# have been transformed into the computer representation shown in Fig. 8. The next job is to
# initialize the queue of output, which is linked together in the QLINK field.) Set R ← 0 and
# QLINK[0] ← 0. For 1 ≤ k ≤ n examine COUNT[k], and if it is zero, set QLINK[R] ← k and R ← k. After
# this has been done for all k, set F ← QLINK[0] (which will contain the first value k encountered
# for which COUNT[k] was zero).
