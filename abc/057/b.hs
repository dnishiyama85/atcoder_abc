import Data.List
import Control.Monad

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  students <- parse 1 n []
  points <- parse 1 m []
  forM_ students $ \st -> print $ findNearest st points

findNearest :: (Int, Int, Int) -> [(Int, Int, Int)] -> Int
findNearest st points = fst $ minimumBy compareDist $ map (\p@(pid, _, _) -> (pid, distance st p)) points

compareDist :: (Int, Int) -> (Int, Int) -> Ordering
compareDist (id1, dist1) (id2, dist2) =
  if dist1 == dist2 then compare id1 id2
                    else compare dist1 dist2

distance :: (Int, Int, Int) -> (Int, Int, Int) -> Int
distance (s, sx, sy) (p, px, py) = abs(sx - px) + abs(sy - py)

parse :: Int -> Int -> [(Int, Int, Int)] -> IO [(Int, Int, Int)]
parse i n carry
  | i == n + 1 = return $ reverse carry
  | otherwise = do
      [a, b] <- (map read . words) <$> getLine :: IO [Int]
      parse (i + 1) n ((i, a, b):carry)
