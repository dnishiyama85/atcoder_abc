import Control.Monad

type Point = (Int, Int)

main :: IO ()
main = do
  [txa, tya, txb, tyb, t, v] <- (map read . words) <$> getLine :: IO [Int]
  n <- readLn :: IO Int
  girls <- replicateM n $ (parse . map read . words) <$> getLine :: IO [Point]
  let a = (txa, tya) :: Point
      b = (txb, tyb) :: Point
      dists = map (distanceThrough a b) girls :: [Float]
      possibles = filter (<= fromIntegral t) $ map (/ fromIntegral v) dists
  putStrLn $ if null possibles then "NO" else "YES"

parse :: [Int] -> Point
parse [x, y] = (x, y)

distanceThrough :: Point -> Point -> Point -> Float
distanceThrough a b p = distance a p + distance p b

distance :: Point -> Point -> Float
distance (ax, ay) (bx, by) =
  sqrt $ fromIntegral ((ax - bx)^2 + (ay - by)^2)
