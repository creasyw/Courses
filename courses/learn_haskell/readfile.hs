import System.IO

import System.IO
main = do
  withFile "girlfriend.txt" ReadMode (\handle -> do
                                         contents <- hGetContents handle
                                         putStr contents)
 
withFile' :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile' path mode f = do
  handle <- openFile path mode
  result <- f handle
  hClose handle
  return result
