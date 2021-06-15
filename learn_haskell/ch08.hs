-- this is interesting... it defines three data types at once
data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving (Show)

surface :: Shape -> Float
surface (Circle _ _ r         ) = pi * r ^ 2
surface (Rectangle x1 y1 x2 y2) = (abs $ x2 - x1) * (abs $ y2 - y1)

-- A more "understandable" way to define - use "Person" to define "Person"
data Person' = Person' String String Int Float String String deriving (Show)

firstName' :: Person' -> String
firstName' (Person' firstname _ _ _ _ _) = firstname

lastName' :: Person' -> String
lastName' (Person' _ lastname _ _ _ _) = lastname

age' :: Person' -> Int
age' (Person' _ _ age _ _ _) = age

height' :: Person' -> Float
height' (Person' _ _ _ height _ _) = height

phoneNumber' :: Person' -> String
phoneNumber' (Person' _ _ _ _ number _) = number

flavor' :: Person' -> String
flavor' (Person' _ _ _ _ _ flavor) = flavor

-- A even better way to make the contructor - it has both getter and setter
data Person = Person
                { firstName   :: String
                , lastName    :: String
                , age         :: Int
                , height      :: Float
                , phoneNumber :: String
                , flavor      :: String
                }
  deriving (Show)

-- This is sick...
-- This can also be the poster boy. It is just insanely easy...
data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
           deriving (Eq, Ord, Show, Read, Bounded, Enum)

-- This type defines three data structures =EmptyTree=, =Node=, and =Tree=
data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

-- Similar to recursive function, it starts from the edge case
singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

-- This is interesting
-- A tree is defined as (Node, Tree, Tree), which is =Node a left right= in the
-- follow function, where =left= and =right= are two trees
treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
    | x == a = Node x left right
    | x < a  = Node a (treeInsert x left) right
    | x > a  = Node a left (treeInsert x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
    | x == a = True
    | x < a  = treeElem x left
    | x > a  = treeElem x right

nums = [8,6,4,1,7,3,5]
-- it can only use =foldr= since the accumulator of the =treeInsert= is at the
-- right side of the two input parameters
numsTree = foldr treeInsert EmptyTree nums
