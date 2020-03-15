-- this is interesting... it defines three data types at once
data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving (Show)

surface :: Shape -> Float
surface (Circle _ _ r)          = pi * r ^ 2
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
