import System.Random

threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen =
  let (first, new) = random gen
      (second, new') = random new
      (third, new'') = random new'
  in (first, second, third)


finiteRandoms :: Int -> StdGen -> ([Int], StdGen)
finiteRandoms 0 g = ([], g)
finiteRandoms n gen =
  let (value, newGen) = random gen
      (restOfList, finalGen) = finiteRandoms (n-1) newGen
  in  (value:restOfList, finalGen)
