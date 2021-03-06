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
    putStrLn $ intercalate " " ["hey", "there", "guys"]
    putStrLn $ intersperse '.' "DOG"
    -- transpose uses the iteration to reverse the row and col of the
    -- list, so it doesn't mind if the list is a 'real' matrix
    putStrLn $ show $ transpose [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    putStrLn $ show $ sum $ takeWhile (< 10000) $ map (^ 3) [1 ..]


-- find how many times each element appears in the list
-- To be a member of Ord, a type must first satisfy the class of Eq
-- countDup :: (Ord a) => [a] -> [(a, Int)]
countDup = map (\l@(x : xs) -> (x, length l)) . group . sort


-- concatMap comes to handy when the function that is about to apply
-- to a list will generate another list, but we still prefer to have
-- only one level of the list after the map
-- rep 4 [1..3] ==> [[1,1,1,1,2,2,2,2,3,3,3,3]]
rep n = concatMap (replicate n)


-- It will fold the entire list and return the accumulator whose
-- initial value is False. The takeWhile is arguably better since it
-- could also deal with infinite lists
search needle haystack =
    let nlen = length needle
    in
        foldl
            (\acc x -> if take nlen x == needle then True else acc)
            False
            (tails haystack)


-- check how many times each element appears in a list
-- the "l" is used to represent the pattern (here is a list) as a
-- whole. It transforms a list into a tuple. The `map` maps every
-- sub-list in the list into a list of tuples.
-- occurance [1,1,1,1,2,2,2,2,3,3,2,2,2,5,6,7]
-- ==> [(1,4),(2,7),(3,2),(5,1),(6,1),(7,1)]
occurance = map (\l@(x : xs) -> (x, length l)) . group . sort


-- neither the "takeWhile" nor the "dropWhile" serve the purpose more
-- efficient than the "any"! This is actually the implementation of
-- "isInfixOf" in the source code, which takes full advantage of laziness
searchInf needle haystack = any (isPrefixOf needle) (tails haystack)


-- use genericlength so that the return type is not explicitly Int
average xs = sum xs / genericLength xs

-- the type signature is required, otherwise, the inference from the
-- complier would deduce this fuction as:
-- zeroCross :: [Integer] -> [[Integer]]
zeroCross :: (Num a, Ord a) => [a] -> [[a]]
-- The condition below is much better than
-- `\x y -> (x>0) && (y>0) || (x<=0) && (y<=0)`
-- A better solution: zeroCross = groupBy (\x y -> (x>0) == (y>0))
zeroCross = groupBy ((==) `on` (> 0))

zeroCross' :: (Num a, Ord a) => [a] -> [[a]]
zeroCross' = groupBy ((==) `on` (> 0))

-- this function performs the same as `words`
sentenceToList = filter (not . any isSpace) . groupBy ((==) `on` isSpace)

-- Caesar cipher
-- It basically does three times of mapping: from msg to the list of
-- ASCII numbers, then to the shifted (coded) ASCII numbers, and
-- finally mapping back to the characters
encode shift msg =
    let
        ords    = map ord msg
        shifted = map (+ shift) ords
    in map chr shifted

decode shift msg = encode (negate shift) msg


-- sample data for list/map example
phoneBook =
    [ ("betty"  , "555-2938")
    , ("bonnie" , "452-2928")
    , ("patsy"  , "493-2928")
    , ("lucille", "205-2928")
    , ("wendy"  , "939-8282")
    , ("penny"  , "853-2492")
    ]

-- `snd` and its counterpart `fst` are similar to `car` and `cdr` in
-- the Racket. `head` will terminate the following evaluation once it
-- find the first match.
findKey key [] = Nothing
findKey key xs = snd . head . filter (\(k, v) -> key == k) $ xs

-- It can also be written as revursive function with edge case as an
-- empty list. Then, splitting a list into a head and a tail,
-- recursive calls -- this is the classic fold pattern!!It's usually
-- better to use folds for this standard list recursion pattern
-- instead of explicitly writing the recursion because they're easier
-- to read and identify.
findKey' key = foldr (\(k, v) acc -> if key == k then Just v else acc) Nothing

fromList' :: (Ord k) => [(k, v)] -> Map.Map k v
fromList' = foldr (\(k, v) acc -> Map.insert k v acc) Map.empty
