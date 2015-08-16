add2 <- function(x, y) {
  x + y
}

above10 <- function(x) {
  use <- x > 10
  x[use]
}

above <- function(x, n = 10) {
  use <- x > n
  x[use]
}

column_mean <- function(y, removena=True) {
  # Get the number of rows
  nc <- ncol(y)
  # Initialize a vector to store the results
  means <- numeric(nc)
  for(i in 1:nc) {
    # Calculate mean with parameter to remove na values
    means[i] <- means(y[, i], na.rm=removena)
  }
  # Just for return the results
  means
}

