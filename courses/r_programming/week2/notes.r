above <- function(x, n=10) {
  x[x>n]
}

columnmean <- function(y, removeNA=TRUE) {
  means <- numeric(ncol(y))
  for (i in 1:ncol(y)) {
    means[i]<-mean(y[,i], na.rm=removeNA)
  }
  means
}   
