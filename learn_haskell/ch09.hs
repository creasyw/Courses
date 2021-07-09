import Control.Monad as Monad
import Data.Char as Char
import Data.List as List
import System.IO as IO
import System.Random as Random

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
-- doesn't work. It is because the Char.toUpper is a "pure function" which could
-- only work on Char, while the IO.getContents returns =IO String=. It needs the
-- =<-= to convert the =IO String= to "regular" string
foreverDo' = do
    l <- IO.getContents
    IO.putStrLn $ map Char.toUpper l


threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen = (first, second, third)
  where (first, newGen) = Random.random gen
        (second, newGen') = Random.random newGen
        (third, _) = Random.random newGen'
