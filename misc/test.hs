module Examples where

square :: Integral a => a -> a
square x = x * x

cubic :: Floating a => a -> a
cubic a = a * a* a

factorial :: (Integral a) => a -> a
factorial x
  | x <= 1 = 1
  | otherwise = x * factorial(x - 1)             

sayMe :: (Integral a) => a -> String
sayMe 1 = "One!"
sayMe 2 = "Two!"
sayMe 3 = "Three!"
sayMe 4 = "Four!"
sayMe 5 = "Five!"
sayMe x = "Not between 1 and 5"

