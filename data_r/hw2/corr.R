corr <- function(directory, threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'threshold' is a numeric vector of length 1 indicating the
    ## number of completely observed observations (on all
    ## variables) required to compute the correlation between
    ## nitrate and sulfate; the default is 0

    ## Return a numeric vector of correlations
    ## NOTE: Do not round the result!

    # mostly copy from complete.R. There must be a better way..
    filenames <- list.files(directory, pattern="*.csv", full.names=TRUE)
    info <- lapply(filenames, read.csv)
    valid_info <- lapply(info, function(k) k[rowSums(is.na(k))<=0,])
    lst <- data.frame("id"=1:length(info), "nobs"=as.vector(Reduce(rbind, lapply(valid_info, nrow))))

    # get ids of the lists that satisfy the threshold
    filtered <- lst[lst["nobs"] > threshold,]["id"]
    # silly indexing....
    filtered <- valid_info[as.list(filtered)[[1]]]
    # dumb type transformation...
    as.vector(Reduce(rbind, lapply(filtered, function(k) cor(k["sulfate"], k["nitrate"]))))
}