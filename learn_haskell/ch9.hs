import Data.Char
import Data.List
import System.Directory
import System.Environment
import System.IO

reverseInput = do
    line <- fmap reverse getLine
    putStrLn $ "You said " ++ line ++ " backward!"
    putStrLn $ "Then, it becomes " ++ line ++ " backwards!"

reverseHyphen = do
    line <- fmap (intersperse '-' . reverse . map toUpper) getLine
    putStrLn line


dispatch = [("add", add), ("view", view), ("remove", remove)]
interactiveTODO = do
    (command : args) <- getArgs
    let (Just action) = lookup command dispatch
    action args

add [fileName, todoItem] = appendFile fileName (todoItem ++ "\n")

view [fileName] = do
    contents <- readFile fileName
    let todoTasks = lines contents
        numberedTasks =
            zipWith (\n line -> show n ++ " - " ++ line) [1 ..] todoTasks
    putStr $ unlines numberedTasks

remove [fileName, numberString] = do
    handle                 <- openFile fileName ReadMode
    (tempName, tempHandle) <- openTempFile "." "temp"
    contents               <- hGetContents handle
    let number       = read numberString - 1
        todoTasks    = lines contents
        newTodoItems = delete (todoTasks !! number) todoTasks
    hPutStr tempHandle $ unlines newTodoItems
    hClose handle
    hClose tempHandle
    renameFile tempName "new_file.txt"
