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
