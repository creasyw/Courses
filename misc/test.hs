module Examples where

square :: Integral a => a -> a
square x = x * x

cubic :: Floating a => a -> a
cubic a = a * a* a

factorial x = product [1..x]

sayMe :: (Integral a) => a -> String
sayMe 1 = "One-1!"
sayMe 2 = "Two-2!"
sayMe 3 = "Three-3!"
sayMe 4 = "Four-4!"
sayMe 5 = "Five-5!"
sayMe x = "Not between 1 and 5"

max' a b
  | a > b = a
  | otherwise = b
                

quicksort lst =
  case lst of
    [] -> []
    (x:xs) -> let smaller = quicksort [a | a <- xs, a <= x]
                  bigger = quicksort[a | a <- xs, a > x]
              in smaller ++ [x] ++ bigger
       
replicate' n x
  | n <= 0 =[]
  | otherwise = x:replicate' (n-1) x

applyt f x =
  f (f x)

largeDivide = head (filter p [100000, 99999..])
  where p x = x `mod` 3829 == 0

-- Collatz sequences
chain n
  | n == 1 = [1]
  | even n = n:chain (n `div` 2)
  | odd n = n:chain (n*3+1)

longerThan n upperbound
  | upperbound <= 0 = 0
  | otherwise = length (filter pred (map chain [1..upperbound]))
                where pred xs = length xs > n

-- use "scanl" to monitor the progress of accumulating
sqrtSum1 = length (takeWhile (<1000) (scanl1 (+) (map sqrt [1..]))) +1


