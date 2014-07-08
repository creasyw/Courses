-- patter matching could be achieve either from repeating the name of
-- the function (in the exactly the same form) or using guards

factorial x
  | x == 1 = 1
  | otherwise = x * factorial (x-1)

length' [] = 0
length' (x:xs) = 1 + length' xs
