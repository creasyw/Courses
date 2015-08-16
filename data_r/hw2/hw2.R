# Question 1
cube <- function(x, n) {
    x^3
}

# Question 3
f <- function(x) {
    g <- function(y) {
        y + z
    }
    z <- 4
    x + g(x)
}