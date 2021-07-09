import System.Environment as Env

main = do
  args <- Env.getArgs
  progName <- Env.getProgName
  putStrLn "The arguments are:"
  mapM putStrLn args
  putStrLn "The program name is:"
  putStrLn progName
