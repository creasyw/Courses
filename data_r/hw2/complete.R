complete <- function(directory, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used

    ## Return a data frame of the form:
    ## id nobs
    ## 1  117
    ## 2  1041
    ## ...
    ## where 'id' is the monitor ID number and 'nobs' is the
    ## number of complete cases

    # list all available filenames
    filenames <- list.files(directory, pattern="*.csv", full.names=TRUE)
    # read the files one by one via lapply
    info <- lapply(filenames, read.csv)
    # slice the interested part
    info <- info[id]

    # filter out na values... the way to describe the function is silly...
    valid_info <- lapply(info, function(k) k[rowSums(is.na(k))<=0,])

    # `lapply` -- calculate the number of rows (nrow) in each list
    # `Reduce` -- combine the separated lists to one list
    # `as.vector` -- change the one-column list to one-row vector
    data.frame("id"=id, "nobs"=as.vector(Reduce(rbind, lapply(valid_info, nrow))))
}