
-- this is a good example of "isolate the impurity to limited exposure of the
-- program" - the function of shortLinesOnly and shortLinesOnly' are pure.
main = do
  contents <- getContents
  putStr (shortLinesOnly' contents)

shortLinesOnly input =
  let allLines = lines input
      shortLines = filter (\line -> length line < 10) allLines
      result = unlines shortLines
  in result

-- The function above is the one given by the book. I'm not a fan of
-- =let...in..= since it feels more like a imperative programming language,
-- while the =where= feels more like a function. But in general, they are doing
-- the same thing.
shortLinesOnly' contents = unlines $ shortLines $ lines contents
  where shortLines input = filter (\line -> length line < 10) input
