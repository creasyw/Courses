import System.Random

threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen =
  let (first, new) = random gen
      (second, new') = random new
      (third, new'') = random new'
  in (first, second, third)

-- The following declaration also works but only for Int output
-- finiteRandoms :: Int -> StdGen -> ([Int], StdGen)

finiteRandoms :: (RandomGen g, Random a, Eq n, Num n) => n -> g -> ([a], g) 
finiteRandoms 0 g = ([], g)
finiteRandoms n gen =
  let (value, newGen) = random gen
      (restOfList, finalGen) = finiteRandoms (n-1) newGen
  in  (value:restOfList, finalGen)
-- e.g. finiteRandoms 3 (mkStdGen 10) :: ([Int], StdGen)
-- output is: ([-2776415066813205131,-8883108635655729860,-2410613080667970943],1143547415 1422611300)
-- or finiteRandoms 5 (mkStdGen 10) :: ([Double], StdGen)
-- output is: ([True,True,True,False,True],1612297749 652912057)
