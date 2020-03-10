maximum' []       = error "Maximum of empty list"
maximum' [x     ] = x
maximum' (x : xs) = max x (maximum' xs)

-- case might be a better way to do input pattern matching
max1 lst = case lst of
    []       -> error "Maximum of empty list"
    [x     ] -> x
    (x : xs) -> max x (max1 xs)

-- Use guards here instead of patterns because it is testing for a boolean
-- condition. Also, the original function signuature is
-- =replicate' :: (Num i, Ord i)=
-- which makes me realize I still haven't fully understand the typeclasses..
replicate' :: (Integral i) => i -> a -> [a]
replicate' n x
    | n <= 0    = []
    | otherwise = x : replicate' (n - 1) x

reverse' []       = []
reverse' (x : xs) = reverse' xs ++ [x]

take' n _        | n <= 0 = []
take' _ []       = []
take' n (x : xs) = x : take' (n - 1) xs

-- first derived function :) Yay!!
-- It actually makes clearer by separating the input cases via pattern matching
-- (e.g. the take' above), compared with using guards (e.g. the =take1= below).
-- The lower implementation also feels more like imperative language than
-- functional language by describing how we do it. However, I still feel the
-- lower case is more aesthetically appealing...
take1 :: (Integral i) => i -> [a] -> [a]
take1 n xs
    | n <= 0         = []
    | length xs == 0 = []
    | otherwise      = first : take1 (n - 1) rest
    where (first : rest) = xs

-- Yes, I agree - it is the post child for Haskell
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x : xs) =
    let
        small = quicksort [ a | a <- xs, a <= x ]
        large = quicksort [ a | a <- xs, a > x ]
    in small ++ [x] ++ large

-- TODO: still not sure how to write local helper function
-- This is a LISP-style tail-recursive function used in the following
splitOn id str acc result
    | length str == 0 = result ++ [acc]
    | head str == id  = splitOn id (tail str) "" (result ++ [acc])
    | otherwise       = splitOn id (tail str) (acc ++ [head str]) result

assemble lst str
    | length lst == 0 = str
    | length str == 0 = assemble (tail lst) (head lst)
    | otherwise       = assemble (tail lst) (str ++ " " ++ (head lst))

reverseWordSeq str = assemble (reverse $ splitOn ' ' str "" []) ""
