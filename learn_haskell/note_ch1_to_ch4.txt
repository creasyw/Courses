For list concatination, Haskell will walk through the whole list at
the left side of the `++`. So, put the longer one at the right will be
a good practice. Or, use the append operation `:` to put the new
element at the head of the original list.

Two lists can be compared! (if the stuff they contain can be compared)
The comparison performs in a lexicographical order.

Haskell has a static type system, in which the type of every
expression is known at compile time. It leads to safer code.

It is a good practice to write the type of a function before actually
implement it, except for the very short ones.

Int and Integer both stand for the type of integers. The difference is
that the latter one is not bounded.

A typeclass can be regarded as an interface that define some
behavior. If a type is a part of a typeclass, that means that it
supports and implement the behavior the typeclass describes.

The pattern matching does not include the keyword "break", and will
always exit after executing any one of the branches. The recommanded
practice of writing cases from specific to general in LISP becomes
mandatory here. Besides, there should always be a "catch-all" pattern
at the end of the matching. Without it, it is possible to terminate
the program while running when it fails to do the pattern matching.

Although guards are similar to pattern matching, but they are fundamentally
different. Every expression behind the guards will return a boolean result,
which in turn dictate whether this branch will be executed. Furthermore, any
condition within guards could use pattern matching to disassemble something, the
result of the matching is either success or failed.

Very similar to where bindings are let bindings. Where bindings are a
syntactic construct that let you bind to variables at the end of a
function and the whole function can see them, including all the
guards. Let bindings let you bind to variables anywhere and are
expressions themselves, but are very local, so they don't span across
guards. Just like any construct in Haskell that is used to bind
values to names, let bindings can be used for pattern matching.

The difference is that let bindings are expressions themselves,
where bindings are just syntactic constructs. That is, for the sake of
pattern matching, let bindings cannot be used cross bars, since they
are expressions and are firely local in the scope.
