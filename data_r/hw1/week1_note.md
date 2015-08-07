- `as.*` explicity coercion

- The concatenate `c(0.6, 0.5)` is similar to the `car` and `cdr` in the Racket. It is also handy by using a vector to define the dimensions of a matrix.
- List use double brackets to access the element, while the vector uses single bracket.
- `Factor` are used to represent categorical data. It follows with some simple statistics summaries.
- `Data Frame` -- the core of the R, as well as Pandas =P
- `names` function will associate vector/list with the names of each column as well as each row.
- R has quite a few different `read` functions to read from csv `read.csv`, `read.table`, `unserialize`, and etc. They also have corresponding writing functions.
- In the reading, specifying the type of the data will accelerate the speed by save the program to figure out by itself.
- Specifying the roughly number of rows will help program optimize the memory usage.
- The filter of the list is weird in R. `x[x > 5]` is the same as `filter(lambda k: k>5, x)` in Python. But it is the same as what is in Pandas.

- The way to filter out NA values of a vector
```
> x <- c(1, 2, NA, 4, 5, NA)
> bad <- is.na(x) # bad: [FALSE FALSE  TRUE FALSE FALSE  TRUE]
> x[!bad]         # !bad: [TRUE  TRUE FALSE  TRUE  TRUE FALSE]
[1] 1 2 4 5
```

#### Logic operators

- ! indicates logical negation (NOT).
- & and && indicate logical AND and | and || indicate logical OR. The shorter form performs elementwise comparisons in much the same way as arithmetic operators. The longer form evaluates left to right examining only the first element of each vector. Evaluation proceeds only until the result is determined. The longer form is appropriate for programming control-flow and typically preferred in if clauses.
- xor indicates elementwise exclusive OR.
- isTRUE(x) is an abbreviation of identical(TRUE, x), and so is true if and only if x is a length-one logical vector with no attributes (not even names).
