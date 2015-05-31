-- curry function
-- regular curry
compareWithHundred :: Integer -> Ordering
compareWithHundred = compare 100

-- curry as infix
dividedByTen = (/10)
dividTen = (10/)

-- the missing variable is at the beginning of original expression
isUpperCase = (`elem` ['A'..'Z'])

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

-- flip the FIRST two arguments of a function
-- Because all functions are curry from the first to the last, so for
-- functions with more than two arguments, "flip'" only has effect on
-- the first two.
flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
  where g x y = f y x
-- another flip with lambda function
flip1 f = \x y -> f y x

map' _ [] = []
map' f (x:xs) = f x : map f xs

filter' _ [] = []
filter' p (x:xs)
  | p x = x : filter p xs
  | otherwise = filter p xs

-- the same quicksort functionality as in the ch5
quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let smaller = quicksort (filter (<=x) xs)
      larger = quicksort (filter (>=x) xs)
  in smaller ++ [x] ++ larger

-- find the largest number under 100000 that's divisible by 3829. The
-- `head` will make the iteration perform until it finds the first
-- value that meets the criterion. LAZINESS!! Besides, the definition
-- of the array is also a good example of defining infinite
-- array. Another side note, the anonymous function could be replaced
-- by a variable and use `where` to define it latter in the code
largestDivisible1 = head (filter (\x -> x `mod` 3829 == 0) [100000, 99999..])

-- dealing with nested list with "map"
testMap =
  let x = [[1,2],[3,4,5,6], [7,8]]
  in map (map (^2)) x

-- example of lazy evaluation
sumOddSquare l = sum (takeWhile (< l) [n^2 | n<-[1..], odd(n^2)])

-- Collatz sequence
chain 1 = [1]
chain n
  | even n = n : chain (div n 2)
  | odd n = n : chain (3*n+1)

-- a good example for the abstraction of calculation process
-- three basic components: predicate, generator, seed. and another three
-- functions piplined to derive the final result
numLongChains = length (filter (\xs-> length xs > 15) (map chain [1..100]))

-- use lazy evaluation and curry to generate a list of functions
listOfFuns = map (*) [0..]
twenty = (listOfFuns !! 4) 5

-- reduce list to a single value with pattern matching of empty list
-- encapsulated into higher order function (folds)
sum1 xs = foldl (\acc x -> acc + x) 0 xs
-- 1. the input variable can be eliminated, and only define the function
-- 2. using curry to make it even more concise
sum2 = foldl (+) 0

elem' y ys = foldl (\acc x -> if x == y then True else acc) False ys

-- an example invoving division and explicit type convertion
-- It's also good to show where is the exact place of accumulator and iterator.
-- Two places to refer: http://bit.ly/1mtqNN2, http://bit.ly/Wva2fr
inconvenientType :: Integral a => [a] -> Float
inconvenientType xs = foldl (\acc k -> acc / (fromIntegral k :: Float)) 1.0 xs

-- more examples of fold
-- they're also good examples of "curry", if the right-most
-- variable(s) of the function body are those needs to input, it's
-- ok/better to left them blank

maximum' :: (Ord a) => [a] -> a
maximum' = foldr1 (\x acc -> if x > acc then x else acc)

reverse' = foldl (\acc x -> x : acc) []
product' = foldr1 (*)

-- filter2 :: (a -> Bool) -> [a] -> a
filter2 p = foldr (\x acc -> if p x then x:acc else acc) []

-- NOTE: there are nontrivial diff between foldl and foldr
  -- foldl :: (a -> b -> a) -> a -> [b] -> a
  -- foldr :: (a -> b -> b) -> b -> [a] -> b
-- It means for "foldl" the accumulator should be the 1st variable in
-- anonymous function, which "foldr" put accumulator in the 2nd place.

-- head and last are also good example for the accumulator.
-- They also make no sense for empty list, so use foldr1/foldl1 instead.
head' = foldr1 (\x _ -> x)
last' = foldl1 (\_ x -> x)

-- exmaple of scans
-- How many elements are there for the sum of roots of all natrual
-- numbers to exceed 1000?
-- it also takes advantage of lazy evaluation.
sqrtSums = length (takeWhile (<1000) (scanl1 (+) (map sqrt [1..]))) + 1

-- ($) could get rid of parentheses, as well as means that function
-- application can be treated just like another function
fancyDollar = map ($ 3) [(4+), (^2), (10*), (*8), sqrt]

functionComp = map (negate . abs) [5, -3, -6, 7, 2, -3]

addSquareSum = sum . takeWhile (<10000) . filter odd $ map (^2) [1..]
