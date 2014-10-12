from math import exp, log, e
from scipy.special import exp1
#average SNR
#average = 0.3162
average = 10

def function(x):
    return 1/x*exp(-x/average)-exp1(x/average)/average

def question_a():
    gamma = 0.0001
    diff_min = abs(1 - function(gamma))
    result = 0
    while gamma<10:
        diff = abs(1 - function(gamma))
        if diff < diff_min:
            diff_min = diff
            result = gamma
        gamma += 0.0001
    print "(a) The gamma_0 is ", result
    return result

def rxtx_csi(x, gamma_0):
    return log(x/gamma_0,2)*exp(-x/average)/average

def question_b():
    gamma_0 = question_a()
    limit = 100
    step = 0.0001
    result = 0
    delta = gamma_0
    while delta < limit:
        result += step*rxtx_csi(delta, gamma_0)
        delta += step
    print "(b) The integral result is ", result*10

def rx_csi(x):
    return log((x+1),2)*exp(-x/average)/average

def question_d():
    limit = 100
    step = 0.0001
    result = 0
    delta = 0
    while delta < limit:
        result += step*rx_csi(delta)
        delta += step
    print "(d) The integral result is ", result*10

if __name__ == "__main__":
    question_b()
    question_d()
