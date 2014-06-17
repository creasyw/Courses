
# Repeatedly append the sum of the current last three elements of lst to lst.
def q09(n):
    sum_three = [0, 1, 2]
    if n <=2:
        return sum_three[n]
    else:
        for i in range(n-2):
            sum_three.append(sum(sum_three[-3:]))
        return sum_three[-1]
