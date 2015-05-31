{-# LANGUAGE NoMonomorphismRestriction #-}
import Data.List
import Data.Function  -- use 'on'
import Data.Char
import qualified Data.Map as Map

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

-- Returns the first stock whose value is no less than 1000. It could
-- deal with infinite list since there is a `head`. Another
-- interesting spot is the pattern matching in lambda function.
firstStock stock = head (dropWhile (\(val, y, m, d) -> val < 1000) stock)

tryout_buildin = do
  putStrLn $ intercalate " " ["hey","there","guys"]
  putStrLn $ intersperse '.' "DOG"
  -- transpose uses the iteration to reverse the row and col of the
  -- list, so it doesn't mind if the list is a 'real' matrix
  putStrLn $ show $ transpose [[1,2,3],[4,5,6],[7,8,9]]
  putStrLn $ show $ sum $ takeWhile (<10000) $ map (^3) [1..]

-- find how many times each element appears in the list
-- To be a member of Ord, a type must first satisfy the class of Eq
-- countDup :: (Ord a) => [a] -> [(a, Int)]
countDup = map (\l@(x:xs) -> (x, length l)) . group . sort

search needle haystack =
  let nlen = length needle
  in foldl (\acc x -> if take nlen x == needle then True else acc) False (tails haystack)

-- use genericlength so that the return type is not explicitly Int
average xs = sum xs / genericLength xs

-- the type signature is required, otherwise, the inference from the
-- complier would deduce this fuction as:
--         zeroCross :: [Integer] -> [[Integer]]
zeroCross :: (Num a, Ord a) => [a] -> [[a]]
zeroCross = groupBy (\x y -> (x>0) == (y>0))

zeroCross' :: (Num a, Ord a) => [a] -> [[a]]
zeroCross' = groupBy ((==) `on` (>0))

sentenceToList = filter (not . any isSpace). groupBy ((==) `on` isSpace)

-- Caesar cipher
encode shift msg =
  let ords = map ord msg
      shifted = map (+ shift) ords
  in map chr shifted

decode shift msg = encode (negate shift) msg

fromList' :: (Ord k) => [(k, v)] -> Map.Map k v
fromList' = foldr (\(k, v) acc -> Map.insert k v acc) Map.empty
