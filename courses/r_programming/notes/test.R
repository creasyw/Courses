myfunction <- function(x) {
    y <- rnorm(100)
    mean(y)
}

second <- function(x) {
    x + rnorm(length(x))
}

matrix_manipulation <- function(x) {
    m <- 1:10
    dim(m) <- c(2,5)
    m
}
