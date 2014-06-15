texasRanges = do
             putStrLn "Generate arithmetic sequences:"
             putStrLn $ show $ take 20 [2, 4..]

             putStrLn "\n List Comprehension:"
             putStrLn $ show [x| x<-[50..100], x `mod` 7 == 3]
             putStrLn $ show [x*y | x<-[1,2,3], y<-[10,20,30]]
             -- Previous one is for itertools.product, but not for
               -- permutations or combinations
             -- putStrLn $ show [(x!!i)*(y!!i) | x<-[1,2,3], y<-[10,20,30], i<-[0,1,2]]

length' xs = sum [1| _ <- xs]
