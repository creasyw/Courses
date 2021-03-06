import           Data.Char

-- basic fucking crazy patten matching
-- It is interesting that only Integral, rather than Num or Fractional, can be
-- used in the signature with the given implementation. My guess is that it
-- relates to pattern matching, but not sure.
-- TODO: check the underlying mechanism of pattern matching
foo :: Integral a => a -> String
foo 5 = "five"
foo x = "not five"

-- patter matching could be achieve either from repeating the name of
-- the function (in the exactly the same form) or using
-- "case". ALthough guards could do similar stuff, it evaluates
-- expressions and returns boolean value deciding if the part of code
-- should be executed.
factorial' :: Integral a => a -> a
factorial' 0 = 1
factorial' x = x * factorial' (x - 1)

factorial :: Integral a => a -> a
factorial x
    | x <= 1    = 1
    | otherwise = x * factorial (x - 1)

length' xs = foldr (\x -> (+) 1) 0 xs

length1 lst = case lst of
    []       -> 0
    (x : xs) -> 1 + length1 xs

-- inline pattern matching with bars
max' a b
    | a > b     = a
    | otherwise = b

-- much more expressive in the expression, and gather all details at
-- one block which is also convenient to read and modify
-- one cannot write a more elegant function :)
bmiTell :: (RealFloat a) => a -> a -> String
bmiTell weight height
    | bmi <= skinny = "You're underweight, you emo, you!"
    | bmi <= normal = "You're supposedly normal. Pffft, I bet you're ugly!"
    | bmi <= fat    = "You're fat! Lose some weight, fatty!"
    | otherwise     = "You're a whale, congratulations!"
  where
    bmi                   = weight / height ^ 2
    (skinny, normal, fat) = (18.5, 25.0, 30.0)

-- input is a list of pair tuples, and the output is a list of floats. It is
-- super cool to use =where= to define the function afterwards. It is the same
-- as layers of abstractions in a math theory
calcBmis :: (RealFloat a) => [(a, a)] -> [a]
calcBmis xs = [ bmi weight height | (weight, height) <- xs ]
    where bmi weight height = weight / height ^ 2

-- let bindings can be treated as expresssions, but where bindings are
-- just syntatic constructs. This makes the let makes more sense in
-- list comprehension
calcBmis1 xs = [ bmi | (w, h) <- xs, let bmi = w / h ^ 2 ]

myCompare :: (Ord a) => a -> a -> Ordering
a `myCompare` b
    | a > b     = GT
    | a == b    = EQ
    | otherwise = LT

-- This is a whole new level of pattern matching for sure. It matches the
-- expression
describeList :: [a] -> String
describeList xs = "The list is" ++ case xs of
    []  -> "empty"
    [_] -> "a singleton list"
    xs  -> "a long list with length " ++ [intToDigit (length xs)]

describeList' :: [a] -> String
describeList' xs = "The list is" ++ what xs
  where
    what []  = "empty"
    what [_] = "a singleton list"
    what xs  = "a long list with length " ++ [intToDigit (length xs)]
