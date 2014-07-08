-- patter matching could be achieve either from repeating the name of
-- the function (in the exactly the same form) or using guards

factorial :: Integral a => a -> a
factorial x
  | x <= 1 = 1
  | otherwise = x * factorial (x-1)

length' [] = 0
length' (x:xs) = 1 + length' xs

max' a b | a > b = a | otherwise = b


bmiTell :: (RealFloat a) => a -> a -> String
bmiTell weight height
  | bmi <= skinny = "You're underweight, you emo, you!"
  | bmi <= normal = "You're supposedly normal. Pffft, I bet you're ugly!"
  | bmi<=fat = "You're fat! Lose some weight, fatty!"
  | otherwise = "You're a whale, congratulations!"
  where bmi = weight / height ^ 2
        (skinny, normal, fat) = (18.5, 25.0, 30.0)

calcBmis :: (RealFloat a) => [(a, a)] -> [a]
calcBmis xs = [bmi weight height | (weight, height) <- xs]
  where bmi weight height = weight / height ^ 2
