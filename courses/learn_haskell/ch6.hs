-- curry function
-- regular curry
compareWithHundred = compare 100

-- curry as infix
dividedByTen = (/10)
dividTen = (10/)

-- the missing variable is in the middle of original expression
isUpperCase = (`elem` ['A'..'Z'])

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
