-- test quicksort
import System.Random
import Data.List

maximum' [] = error "Maximum of empty list"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)

-- case might be a better way to do input pattern matching
max1 lst =
  case lst of [] -> error "Maximum of empty list"
              [x] -> x
              (x:xs)-> max x (max1 xs)

reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

take' n _ | n<=0 = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs

quicksort [] = []
quicksort (x:xs) =
  let small = quicksort [a | a <- xs, a <= x]
      large = quicksort [a | a <- xs, a > x]
  in small ++ [x] ++ large

testQuicksort n = do
  seed  <- newStdGen
  let rs = randomList n seed
  putStrLn "Before sorting:"
  print rs
  putStrLn "After the sort"
  print $ quicksort rs

randomList :: Int -> StdGen -> [Int]
randomList n = take n . unfoldr (Just . random)

-- TODO: still not sure how to write local helper function
-- This is a LISP-style tail-recursive function used in the following
splitOn id str acc result
  | length str == 0 = result ++ [acc]
  | head str == id = splitOn id (tail str) "" (result ++ [acc])
  | otherwise = splitOn id (tail str) (acc ++ [head str]) result

assemble lst str
  | length lst == 0 = str
  | length str == 0 = assemble (tail lst) (head lst)
  | otherwise = assemble (tail lst) (str++" "++(head lst))

reverseWordSeq str = assemble (reverse $ splitOn ' ' str "" []) ""
