maximum' [] = error "Maximum of empty list"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)

reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

quicksort [] = []
quicksort (x:xs) =
  let small = quicksort [a | a <- xs, a <= x]
      large = quicksort [a | a <- xs, a > x]
  in small ++ [x] ++ large

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
