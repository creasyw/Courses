maximum' [] = error "Maximum of empty list"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)

reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]
