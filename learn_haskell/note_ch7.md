>To import a module, it is different in the file from in the repl. In a
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

The `on` in the `Data.Function` is an elegant way to combine several
results from previous functions together. It acts like `reduce`, but
in a smarter way:)

     (*) `on` f = \x y -> f x * f y.



## [Explain `Just`, `Nothing`, and `Maybe`](http://stackoverflow.com/questions/18808258/what-does-the-just-syntax-mean-in-haskell)

It's actually just a normal type constructor that happens to be
defined in the *Prelude*, which is the standard library that is
imported automatically into every module.

## What Maybe is, Structurally

The definition looks something like this:

    data Maybe a = Just a
                     | Nothing

That declaration defines a type, `Maybe a`, which is parameterized by
a type variable `a`, which just means that you can use it with any
type in place of `a`.

### Constructing and Destructing

The type has two constructors, `Just a` and `Nothing`. When a type has
multiple constructors, it means that a value of the type must have
been constructed with just one of the possible constructors. For this
type, a value was either constructed via `Just` or `Nothing`, there
are no other (non-error) possibilities.

Since `Nothing` has no parameter type, when it's used as a constructor
it names a constant value that is a member of type `Maybe a` for all
types `a`. But the `Just` constructor does have a type parameter,
which means that when used as a constructor it acts like a function
from type `a` to `Maybe a`, i.e. it has the type `a -> Maybe a`

So, the constructors of a type build a value of that type; the other
side of things is when you would like to use that value, and that is
where pattern matching comes in to play. Unlike functions,
constructors can be used in pattern binding expressions, and this is
the way in which you can do *case analysis* of values that belong to
types with more than one constructor.

In order to use a `Maybe a` value in a pattern match, you need to
provide a pattern for each constructor, like so:

    case maybeVal of
            Nothing   -> "There is nothing!"
                    Just val  -> "There is a value, and it is " ++
            (show val)

In that case expression, the first pattern would match if the value
was `Nothing`, and the second would match if the value was constructed
with `Just`.  If the second one matches, it also binds the name `val`
to the parameter that was passed to the `Just` constructor when the
value you're matching against was constructed.

### What Maybe Means

Maybe you were already familiar with how this worked; there's not
really any magic to `Maybe` values, it's just a normal Haskell
Algebraic Data Type (ADT). But it's used quite a bit because it
effectively "lifts" or extends a type, such as `Integer` from your
example, into a new context in which it has an extra value (`Nothing`)
that represents a lack of value! The type system then requires that
you check for that extra value before it will let you get at the
`Integer` that *might* be there. This prevents a remarkable number of
bugs.

Many languages today handle this sort of "no-value" value via NULL
references. Tony Hoare, an eminent computer scientist (he invented
Quicksort and is a Turing Award winner), owns up to this as his
["billion dollar
mistake"](http://qconlondon.com/london-2009/presentation/Null+References:+The+Billion+Dollar+Mistake).
The `Maybe` type is not the only way to fix this, but it has proven to be an
effective way to do it.

### Maybe as a Functor

The idea of transforming one type to another one such that operations
on the old type can *also* be transformed to work on the new type is
the concept behind the Haskell type class called `Functor`, which
`Maybe a` has a useful instance of.

`Functor` provides a method called `fmap`, which maps functions that
range over values from the base type (such as `Integer`) to functions
that range over values from the lifted type (such as `Maybe
Integer`). A function transformed with `fmap` to work on a `Maybe`
value works like this:

    case maybeVal of
          Nothing  -> Nothing         -- there is nothing, so just
          return Nothing
                Just val -> Just (f val)    -- there is a value, so
          apply the function to it

So if you have a `Maybe Integer` value `m_x` and an `Int -> Int`
function `f`, you can do `fmap f m_x` to apply the function `f`
directly to the `Maybe Integer` without worrying if it's actually got
a value or not. In fact, you could apply a whole chain of lifted
`Integer -> Integer` functions to `Maybe Integer` values and only have
to worry about explicitly checking for `Nothing` once when you're
finished.

### Maybe as a Monad

I'm not sure how familiar you are with the concept of a `Monad` yet,
but you have at least used `IO a` before, and the type signature `IO
a` looks remarkably similar to `Maybe a`. Although `IO` is special in
that it doesn't expose its constructors to you and can thus only be
"run" by the Haskell runtime system, it's still also a `Functor` in
addition to being a `Monad`.  In fact, there's an important sense in
which a `Monad` is just a special kind of `Functor` with some extra
features, but this isn't the place to get into that.

Anyway, Monads like `IO` map types to new types that represent
"computations that result in values" and you can lift functions into
`Monad` types via a very `fmap`-like function called   `liftM` that
turns a regular function into a "computation that results in the value
obtained by evaluating the function."

You have probably guessed (if you have read this far) that `Maybe` is
also a `Monad`. It represents "computations that could fail to return
a value". Just like with the `fmap` example, this lets you do a whole
bunch of computations without having to explicitly check for errors
after each step. And in fact, the way the `Monad` instance is
constructed, a computation on `Maybe` values *stops* as soon as a
`Nothing` is encountered, so it's kind of like an immediate abort or a
valueless return in the middle of a computation.
