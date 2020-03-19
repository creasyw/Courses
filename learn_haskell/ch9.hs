import Control.Monad as Monad
import Data.Char as Char
import Data.List
import System.Directory
import System.Environment
import System.IO as IO

reverseInput = do
    line <- IO.getLine
    IO.putStrLn $ "You said " ++ line ++ " backward!"
    IO.putStrLn $ "Then, it becomes " ++ reverse line ++ " backwards!"

reverseHyphen = do
    -- similar to `map`, `fmap` is the functor to map IO:Stream to another form
    line <- fmap (intersperse '-' . reverse . map Char.toUpper) IO.getLine
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

-- dispatch = [("add", add), ("view", view), ("remove", remove)]
-- interactiveTODO = do
--     (command : args) <- getArgs
--     let (Just action) = lookup command dispatch
--     action args
--
-- add [fileName, todoItem] = appendFile fileName (todoItem ++ "\n")
--
-- view [fileName] = do
--     contents <- readFile fileName
--     let todoTasks = lines contents
--         numberedTasks =
--             zipWith (\n line -> show n ++ " - " ++ line) [1 ..] todoTasks
--     putStr $ unlines numberedTasks
--
-- remove [fileName, numberString] = do
--     handle                 <- openFile fileName ReadMode
--     (tempName, tempHandle) <- openTempFile "." "temp"
--     contents               <- hGetContents handle
--     let number       = read numberString - 1
--         todoTasks    = lines contents
--         newTodoItems = delete (todoTasks !! number) todoTasks
--     hPutStr tempHandle $ unlines newTodoItems
--     hClose handle
--     hClose tempHandle
--     renameFile tempName "new_file.txt"
