import Control.Monad as Monad
import Data.Char as Char
import Data.List as List
import System.IO as IO

reverseInput = do
    line <- IO.getLine
    IO.putStrLn $ "You said " ++ line ++ " backward!"
    IO.putStrLn $ "Then, it becomes " ++ reverse line ++ " backwards!"

reverseHyphen = do
    -- similar to `map`, `fmap` is the functor to map IO:Stream to another form
    line <- fmap (List.intersperse '-' . reverse . map Char.toUpper) IO.getLine
    IO.putStrLn line

foreverDo = Monad.forever $ do
    IO.putStr "Give me some input: "
    l <- IO.getLine
    IO.putStrLn $ map toUpper l

-- I tried a one-liner =IO.putStrLn $ fmap Char.toUpper IO.getContents= and it
-- doesn't work. It seems that the IO:Stream has to have a place-holder for
-- further processing
foreverDo' = do
    l <- IO.getContents
    IO.putStrLn $ map Char.toUpper l
