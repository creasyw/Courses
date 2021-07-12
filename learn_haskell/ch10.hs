import Data.List as List

-- the `Maybe` makes teh function tolerate bad input
solveRPN :: String -> Float
solveRPN = head . foldl foldingFunction [] . words
  where
    -- interesting to make the pattern matching within the =where=
    foldingFunction (x : y : ys) "*"          = (x * y) : ys
    foldingFunction (x : y : ys) "+"          = (x + y) : ys
    foldingFunction (x : y : ys) "-"          = (x - y) : ys
    -- sometime, the stupidity of the strick typeclass shows itself, e.g. now.
    -- it as `/` vs `div`, and `**` vs `^`, just to make them operate on float
    -- or int numbers
    foldingFunction (x : y : ys) "/"          = (x / y) : ys
    foldingFunction (x : y : ys) "^"          = (y ** x) : ys
    foldingFunction (x     : xs) "ln"         = log x : xs
    foldingFunction xs           "sum"        = [sum xs]
    -- make the numbers in a stack so that the previous operation could act on
    -- the first two numbers of the existing stack
    foldingFunction xs           numberString = read numberString : xs

data Node = Node Road (Maybe Road)
data Road = Road Int Node
data Section = Section { getA :: Int, getB :: Int, getC :: Int } deriving (Show)
type RoadSystem = [Section]

heathrowToLondon :: RoadSystem
heathrowToLondon =
    [Section 50 10 30, Section 5 90 20, Section 40 2 25, Section 10 8 0]

data Label = A | B | C deriving (Show)
type Path = [(Label, Int)]

roadStep :: (Path, Path) -> Section -> (Path, Path)
roadStep (pathA, pathB) (Section a b c) =
    let
        priceA          = sum $ map snd pathA
        priceB          = sum $ map snd pathB
        forwardPriceToA = priceA + a
        crossPriceToA   = priceB + b + c
        forwardPriceToB = priceB + b
        crossPriceToB   = priceA + a + c
        newPathToA      = if forwardPriceToA <= crossPriceToA
            then (A, a) : pathA
            else (C, c) : (B, b) : pathB
        newPathToB = if forwardPriceToB <= crossPriceToB
            then (B, b) : pathB
            else (C, c) : (A, a) : pathA
    in (newPathToA, newPathToB)

optimalPath :: RoadSystem -> Path
optimalPath roadSystem =
    let (bestAPath, bestBPath) = foldl roadStep ([], []) roadSystem
    in
        if sum (map snd bestAPath) <= sum (map snd bestBPath)
            then reverse bestAPath
            else reverse bestBPath

groupsOf :: Int -> [a] -> [[a]]
groupsOf 0 _  = undefined
groupsOf _ [] = []
groupsOf n xs = take n xs : groupsOf n (drop n xs)

main = do
    contents <- getContents
    let threes     = groupsOf 3 (map read $ lines contents)
        roadSystem = map (\[a, b, c] -> Section a b c) threes
        path       = optimalPath roadSystem
        pathString = concatMap (show . fst) path
        pathPrice  = sum $ map snd path
    putStrLn $ "The best path to take is: " ++ pathString
    putStrLn $ "The price is: " ++ show pathPrice
