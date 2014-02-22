# Consider the measurements
# 
# x[n] = r_n + w[n],
# 
# where w[n] is zero-mean Gaussian with variance \delta^2. Generate this data for
# a value of r that you want; selected such that 0 < r < 1 and generate noise for
# variance σ2 = 10^{-3}. Generate N = 50 data and apply Newton-Raphson (N-R) to
# find the MLE and check how close it gets to the value you selected for r. 
# Generate multiple batches (say M = 50) of N = 50 data and apply N-R for each
# different batch. Keep the M different estimates you get for r and average them
# out in order to obtain an estimate for the mean and the variance. Follow the
# same process for different increasing values of N. Do you observe the
# asymptotic efficiency of the MLE for r? Where does the mean and variance
# converge to as you increase N?
