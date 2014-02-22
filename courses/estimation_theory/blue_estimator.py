# Consider the source localization problem studied in class. Let the source be 
# located at position (xs, ys) = (10, 20) and suppose that the reference time 
# \tau_0 = 0. You are going to use this location to generate the measurements 
# t_i using the nonlinear model described in class. To do that you will have to 
# place at the positions you want N sensors (the number N will be input in your 
# program along with the positions of the sensors {(xi, yi)}^N_i=1
# 
# Using the linearization approach described in class use the BLUE to find the 
# source location estimate (x_s, y_s).
# 
# You can try different selections for the nominal source location (xn,yn) which 
# is needed to perform linearization. Try values that are close to the true 
# position (x , y ), as well as far to see how the localization error 
# (xˆs − xs)2 + (yˆs − ys)2 is affected.
# 
# The goal is to plot the localization error as a function of the number of 
# sensors used. Try values N = 3 : 2 : 30. For each value of N fix (xn, yn), 
# and run your method multiple times where every time you place the sensors at 
# different locations and you generate a different set of measurements ti. 
# Perform 100 different runs (Monte Carlo iterations) for each value of N and 
# then save the 100 different localization errors you get and average them. 
# Then, plot the average localization error for each value of N. Perform this 
# process for small noise variance σ2 = 10−2, and relatively large variance 
# \delta^2 = 0.1.

