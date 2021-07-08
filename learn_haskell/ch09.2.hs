import Data.Char as Char

main = do
  contents <- getContents
  putStrLn (map Char.toUpper contents)
