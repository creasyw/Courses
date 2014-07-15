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
