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

map' _ [] = []
map' f (x:xs) = f x : map f xs

filter' _ [] = []
filter' p (x:xs)
  | p x = x : filter p xs
  | otherwise = filter p xs

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

-- reduce list to a single value with pattern matching of empty list
-- encapsulated into higher order function (folds)
sum1 xs = foldl (\acc x -> acc + x) 0 xs
-- using curry to make it even more concise
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
