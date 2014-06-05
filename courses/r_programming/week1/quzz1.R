sol <- function() {
    x <- read.table("hw1_data.csv", header=TRUE, sep=",")

    writeLines("\nQuestion 11:")
    print(names(x))

    writeLines("\nQuestion 12:")
    print(x[1:2,])

    writeLines("\nQuestion 13:")
    print(dim(x)[1])

    writeLines("\nQuestion 14:")
    print(x[(dim(x)[1]-1):dim(x)[1],])

    writeLines("\nQuestion 15:")
    print(x[47, "Ozone"])

    writeLines("\nQuestion 16:")
    y <- x[,"Ozone"]
    print(length(y[is.na(y)]))

    writeLines("\nQuestion 17:")
    print(mean(y[!is.na(y)]))

    writeLines("\nQuestion 18:")
    y <- x[!is.na(x[,"Ozone"]),]
    y <- y[!is.na(y[,"Temp"]), ]
    y <- y[y[,"Ozone"]>31 & y[,"Temp"]>90,][,"Solar.R"]
    print(mean(y[!is.na(y)]))

    writeLines("\nQuestion 19:")
    y <- x[!is.na(x[,"Month"]),]
    y <- y[y[,"Month"]==6,][,"Temp"]
    print(mean(y[!is.na(y)]))

    writeLines("\nQuestion 19:")
    y <- x[!is.na(x[,"Month"]),]
    y <- y[y[,"Month"]==5,][,"Ozone"]
    print(max(y[!is.na(y)]))

}

