removeNonUppercase st = [ c | c<- st, elem c ['A'..'Z']]
