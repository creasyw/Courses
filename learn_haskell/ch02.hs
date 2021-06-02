texasRanges = do
    putStrLn "Generate arithmetic sequences:"
    putStrLn $ show $ take 20 [2, 4 ..]

    putStrLn "\n List Comprehension:"
    putStrLn $ show [ x | x <- [50 .. 100], x `mod` 7 == 3 ]
    putStrLn $ show [ x * y | x <- [1, 2, 3], y <- [10, 20, 30] ]
             -- Previous one is for itertools.product, but not for
               -- permutations or combinations
             -- putStrLn $ show [(x!!i)*(y!!i) | x<-[1,2,3], y<-[10,20,30], i<-[0,1,2]]

length' xs = sum [ 1 | _ <- xs ]
triangular xs =
    [ (a, b, c)
    | c <- xs
    , b <- [1 .. c]
    , a <- [1 .. b]
    , a ^ 2 + b ^ 2 == c ^ 2
    ]

square :: Integral a => a -> a
square x = x * x

cubic :: Floating a => a -> a
cubic a = a * a * a

factorial x = product [1 .. x]

sayMe :: (Integral a) => a -> String
sayMe 1 = "One-1!"
sayMe 2 = "Two-2!"
sayMe 3 = "Three-3!"
sayMe 4 = "Four-4!"
sayMe 5 = "Five-5!"
sayMe x = "Not between 1 and 5"

max' a b
    | a > b     = a
    | otherwise = b


-- nice example for both list, pattern matching, AND recursion
quicksort lst = case lst of
    [] -> []
    (x : xs) ->
        let
            smaller = quicksort [ a | a <- xs, a <= x ]
            bigger  = quicksort [ a | a <- xs, a > x ]
        in smaller ++ [x] ++ bigger

replicate' n x
    | n <= 0    = []
    | otherwise = x : replicate' (n - 1) x

applyt f x = f (f x)

-- Lazy evaluate the initial list of input
largeDivide = head (filter p [100000, 99999 ..]) where p x = x `mod` 3829 == 0

-- Collatz sequences
-- Guards is for conditions, versus the pattern matching above
chain n
    | n == 1 = [1]
    | even n = n : chain (n `div` 2)
    | odd n  = n : chain (n * 3 + 1)

longerThan n upperbound
    | upperbound <= 0 = 0
    | otherwise       = length (filter pred (map chain [1 .. upperbound]))
    where pred xs = length xs > n

-- use "scanl" to monitor the progress of accumulating
sqrtSum1 = length (takeWhile (< 1000) (scanl1 (+) (map sqrt [1 ..]))) + 1
