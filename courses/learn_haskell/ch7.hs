import Data.List

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

tryout_buildin = do
  putStrLn $ intercalate " " ["hey","there","guys"]
  putStrLn $ intersperse '.' "DOG"
  -- transpose uses the iteration to reverse the row and col of the
  -- list, so it doesn't mind if the list is a 'real' matrix
  putStrLn $ show $ transpose [[1,2,3],[4,5,6],[7,8,9]]
  putStrLn $ show $ sum $ takeWhile (<10000) $ map (^3) [1..]

-- find how many times each element appears in the list
-- this function needs EXPLICIT typeclass signature within the type declaration.
-- To be a member of Ord, a type must first satisfy the class of Eq
countDup :: (Ord a) => [a] -> [(a, Int)]
countDup = map (\l@(x:xs) -> (x, length l)) . group . sort

search needle haystack =
  let nlen = length needle
  in foldl (\acc x -> if take nlen x == needle then True else acc) False (tails haystack)

-- use genericlength so that the return type is not explicitly Int
average xs = sum xs / genericLength xs
