# Algorithm A (Multiply permutations in cycle form). This algorithm takes a product of cycles, such
# as (6), and computes the resulting permutation in the form of a product of disjoint cycles. For
# simplicity, the removal of singleton cycles is not described here; that would be a fairly simple
# extension of the algorithm. As this algorithm is performed, we successively “tag” the elements of
# the input formula; that is, we mark somehow those symbols of the input formula that have been
# processed.
#
# A1. [First pass.] Tag all left parentheses, and replace each right parenthesis by a tagged copy of
# the input symbol that follows its matching left parenthesis. (See the example in Table 1.)
# A2. [Open.] Searching from left to right, find the first untagged element of the input. (If all
# elements are tagged, the algorithm terminates.) Set START equal to it; output a left parenthesis;
# output the element; and tag it.
# A3. [Set CURRENT.] Set CURRENT equal to the next element of the formula.
# A4. [Scan formula.] Proceed to the right until either reaching the end of the formula, or finding
# an element equal to CURRENT; in the latter case, tag it and go back to step A3.
# A5. [CURRENT = START?] If CURRENT ≠ START, output CURRENT and go back to step A4 starting again at
# the left of the formula (thereby continuing the development of a cycle in the output).
# A6. [Close.] (A complete cycle in the output has been found.) Output a right parenthesis, and go
# back to step A2.
#
# Algorithm B (Multiply permutations in cycle form). This algorithm accomplishes essentially the
# same result as Algorithm A. Assume that the elements permuted are named x1, x2, ..., xn. We use an
# auxiliary table T [1], T [2], ..., T [n]; upon termination of this algorithm, xi goes to xj under
# the input permutation if and only if T[i] = j.
# B1. [Initialize.] Set T[k] ← k for 1 ≤ k ≤ n. Also, prepare to scan the input from right to left.
# B2. [Next element.] Examine the next element of the input (right to left). If the input has been
# exhausted, the algorithm terminates. If the element is a “)”, set Z ← 0 and repeat step B2; if it
# is a “(”, go to B4. Otherwise the element is xi for some i; go on to B3.
# B3. [Change T [i].] Exchange Z ↔ T [i]. If this makes T [i] = 0, set j ← i. Return to step B2.
# B4. [Change T [j].] Set T [j] ← Z. (At this point, j is the row that shows a “)” entry in the
# notation of Table 2, corresponding to the right parenthesis that matches the left parenthesis just
# scanned.) Return to step B2.
