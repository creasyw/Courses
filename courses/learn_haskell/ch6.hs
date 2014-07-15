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
