main = do
  line <- getLine
  putStrLn $ reverseWord line

reverseWord = unwords . map reverse . words
