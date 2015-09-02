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

# [`foldl`, `foldr`, and `folds`](https://wiki.haskell.org/Foldr_Foldl_Foldl')

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

Because of GHC's lazy reduction strategy -- expressions are reduced
only when they are actually needed -- both `foldl` and `foldr` will
suffer the stack overflow if evaluates a list too large for the
current memory of the system, **if the evaluation function cannot be
_lazy_**. In this case, the outer-left-most
redexes are reduced first. In this case it's the outer foldl (+)
... [1..10000] redexes which are repeatedly reduced. So the inner z1,
z2, z3, ... redexes only get reduced when the foldl is completely gone.

Usually the choice is between foldr and foldl', since foldl and foldl'
are the same except for their strictness properties, so if both return
a result, it must be the same. foldl' is the more efficient way to
arrive at that result because it doesn't build a huge thunk. However,
**if the combining function is lazy in its first argument, foldl may
happily return a result where foldl' hits an exception.**

In general, the `foldr` is most commonly used when transforming lists
(or other foldables) into lists with related elements in the same
order. It is also effective to transform infinite lists into other
infinite lists (*TODO* example needed...).

The other very useful fold is `foldl'`. It can be thought of as a `foldr`
with these differences:

- `foldl'` conceptually reverses the order of the list. One consequence is
that a `foldl'` (unlike `foldr`) applied to an infinite list will be
bottom; it will not produce any usable results, just as an express
reverse would not. Note that `foldl' (flip cons) []==reverse`.
- `foldl'` often has much better time and space performance than a `foldr`
would for the reasons explained in the previous sections.

`foldl'` should be picked principally in two cases:

- When the list to which it is applied is large, but definitely finite,
you do not care about the implicit reversal (for example, because your
combining function is commutative like (+), (*), or Set.union), and
you seek to improve the performance of your code.
- When you actually do want to reverse the order of the list, in
addition to possibly performing some other transformation to the
elements. In particular, if you find that you precede or follow your
fold with a reverse, it is quite likely that you could improve your
code by using the other fold and taking advantage of the implicit
reverse.

**`foldl` is rarely the right choice. It gives you the implicit reverse of
fold, but without the performance gains of `foldl'`.** (really?!)

Another reason that `foldr` is often the better choice is that the
folding function can **short-circuit**, that is, terminate early by
yielding a result which does not depend on the value of the
accumulating parameter. When such possibilities arise with some
frequency in your problem, short-circuiting can greatly improve your
program's performance. Left folds can never short-circuit.

To illustrate this consider writing a fold that computes the product
of the last digits of a list of integers. One might think that `foldl'`
is the superior fold in this situation as the result does not depend
on the order of the list and is generally not computable on infinite
lists anyway.
