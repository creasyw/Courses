# Apply function to each element in a list
x <- list(a=1:4, b=rnorm(10), c=rnorm(20, 2))
y <- lapply(x, mean)
print(y)

# split a vector according to specific rules. It can also perform
# multi-levels split via concatenate different rules into a list of
# rules, and then split the vector according to this list
x <- c(rnorm(10), runif(10), rnorm(10, 1))
# rules
rs <- gl(3, 10)
result <- split(x, f)