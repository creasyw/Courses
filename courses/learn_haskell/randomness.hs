import System.Random

threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen =
  let (first, new) = random gen
      (second, new') = random new
      (third, new'') = random new'
  in (first, second, third)

finiteRandoms :: (Num n, Eq n, RandomGen g, Random a) => n -> g -> ([a], g)
finiteRandoms 0 gen = ([], gen)
finiteRandoms n gen =
  let (value, newGen) = random gen
      (restOfList, finalGen) = finiteRandoms (n-1) newGen
  in  (value:restOfList, finalGen)
