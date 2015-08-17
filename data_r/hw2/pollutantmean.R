pollutantmean <- function(directory, pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files

    ## 'pollutant' is a character vector of length 1 indicating
    ## the name of the pollutant for which we will calculate the
    ## mean; either "sulfate" or "nitrate".
    
    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used

    ## Return the mean of the pollutant across all monitors list
    ## in the 'id' vector (ignoring NA values)
    ## NOTE: Do not round the result!

    # list all available filenames
    filenames <- list.files(directory, pattern="*.csv", full.names=TRUE)
    # read the files one by one via lapply
    info <- lapply(filenames, read.csv)
    # reduce/concatenate the interested data
    info <- Reduce(rbind, info[id])

    # fuck it! It is so awkward
    # STUPID FEATURE ALERT: this is not working: mean(sliced$pollutant, na.rm=TRUE)
    mean(info[,pollutant], na.rm=TRUE)
}