To import a module, it is different in the file from in the repl. In a
script, it is similar to what Python dose `import <module name>`, and
in the repl `ghci> :m + <module name>`.

A useful tip to deal with name collision is that `import qualified
<module name> as <abbreviation>`. In this manner, if we call a
function `foo`, it is locally defined, while the `<abbreviation>.foo`
is defined in the module.

"A great way to pick up new Haskell knowledge is to just click through
the standard library reference and explore the modules and their
functions. You can also view the Haskell source code for each
module. Reading the source code of some modules is a really good way
to learn Haskell and get a solid feel for it. -- To search for
functions or to find out where they're located, use Hoogle."

foldl' and foldl1' are stricter versions of their respective lazy
incarnations. When using lazy folds on really big lists, you might
often get a stack overflow error. The culprit for that is that due to
the lazy nature of the folds, the accumulator value isn't actually
updated as the folding happens. What actually happens is that the
accumulator kind of makes a  promise that it will compute its value
when asked to actually produce the result (also called a thunk). That
happens for every intermediate accumulator and all those thunks
overflow your stack. The strict folds aren't lazy buggers and actually
compute the intermediate values as they go along instead of filling up
your stack with thunks. So if you ever get stack overflow errors when
doing lazy folds, try switching to their strict versions.

- It reveals a pros/cons for lazy evaluation. That is, it will save
  the computation resources and apply it only when necessary; but on
  the ohter hand, it requires more memory to store the intermediate
  stages so that the program could remember where to start.

Concatenation `concat` only remove one level of nesting.

There are also functions generating infinite list, such as
`iterate`. As a result, it is supposed to run with other functions to
truncate the resulting list, such as `take` or `takeWhile`.

The `span` and `break` will break a list into two parts at the 1st
time that the requirement is fulfilled, while the `partition` will
scan through the entire list.

`isInfixof` is good to find if one list is a subset of another list.

`zip` will pack two list as one list with the length of the shorter
list and every element is the tuple containing two items from both
lists. `zipWith` can do more. It merge two lists into one by
performing operations defined as anonymous function.

What length, take, drop, splitAt, !! and replicate have in common is
that they take an Int as one of their parameters (or return an Int),
even though they could be more generic and usable if they just took
any type that's part of the Integral or Num typeclasses (depending on
the functions). They do that for historical reasons. However, fixing
that would probably break a lot of existing code. That's why Data.List
has their more generic equivalents, named genericLength, genericTake,
genericDrop, genericSplitAt, genericIndex and genericReplicate. For
instance, length has a type signature of length :: [a] -> Int. If we
try to get the average of a list of numbers by doing let xs = [1..6]
in sum xs / length xs, we get a type error, because you can't use /
with an Int. genericLength, on the other hand, has a type signature of
genericLength :: (Num a) => [b] -> a. Because a Num can act like a
floating point number, getting the average by doing let xs = [1..6] in
sum xs / genericLength xs works out just fine.

The nub, delete, union, intersect and group functions all have their
more general counterparts called nubBy, deleteBy, unionBy, intersectBy
and groupBy. The difference between them is that the first set of
functions use == to test for equality, whereas the By ones also take
an equality function and then compare them by using that equality
function. group is the same as groupBy (==).
