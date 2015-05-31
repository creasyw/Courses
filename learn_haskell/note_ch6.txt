A FP has higher-order function, which either (or both) take functions
as parameters and return functions as return values. It is critical
for defining the computation processes.

ALL Haskell functions only take one argument a time, then apply curry
to complete all partially applied function step by step.

If a function is fed with too few parameters, it becomes a "partially
applied" function. If is a neat way to create functions on the fly so
it can be passed into another function, or just to seed them with some
basic data.

Infix functions make the curry even more flexible. Surrounded the
expression with parentheses and only supply a parameter on one side

The `map` functions could also be performed by list comprehension, but
the former method is more readable to apply a complicated function to
a list. In some cases, map a map to a list of list is awesome:) The
same rule of thumb also applies to "filter versus list
comprehension". When it deals with multiple predicates (such as mixing
logical and function predicates), the filter is better than the LC.

For the purpose of feeding higher-order function an anonymous
function, the 1st thing to consider is curry rather than the
lambda. For example, the following two function are the same and the
former one is better.

map (+3) [1..10]
map (\x -> x+3) [1..10]

Lambda can also perform pattern matching.

foldl has (\acc x -> ...) and the foldr has (\x acc -> ...). It is
"kind of" making sense because foldl is folding the list from left, so
the accumulator is in the left, and vice versa for folding from
right. A more interesting usage is to operate foldr towards an
infinite list. Apply the foldr to this list at SOME POINT, and then
fold them from the right.

Folds can be used to implement any function where you traverse a list
once, element by element, and then return something based on
that. Whenever you want to traverse a list to return something,
chances are you want a fold.

Scan is similar to fold, but is able to monitor the intermediate
results. This is another function **facilitates** lazy evaluation,
which mean "it will fold until a certain point". The similar
alternatives involves filter and takeWhile.

For list operation, the concatenation ++ is much more expensive than
the append :. They are just the opposite to the Python implementation.

Another important concept is the '$' function application, which makes
the default left-associative function to right-associative. Besides,
it also means that function application can be treated as another
function, which can be `map` over a list of functions.

The counterpart is the dot '.' as function composition. It works as
the function composition in the math derivation. One of the uses is to
create new function on the fly. It should be more concise and clearer
semantically than the anonymous function. If we want to apply function
composition to the function requires several input parameters, the
curry comes handy, That is, we have to partially apply the function to
only accept one input parameter, then it can be put into the chain of
function composition.
