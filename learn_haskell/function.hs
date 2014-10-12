import Data.Char
import Data.List

reverseInput = do line <- fmap reverse getLine
                  putStrLn $ "You said " ++ line ++ " backward!"
                  putStrLn $ "Then, it becomes " ++ line ++ " backwards!"

reverseHyphen = do line <- fmap (intersperse '-' . reverse . map toUpper) getLine
                   putStrLn line
