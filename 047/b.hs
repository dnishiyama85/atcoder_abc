import Control.Monad

main :: IO ()
main = do
  [w, h, n] <- (map read . words) <$> getLine :: IO [Int]
  rows <- replicateM n $ (map read . words) <$> getLine :: IO [[Int]]
  let left   = maximum $ map (\[x, y, a] -> x) $ filter (\[x, y, a] -> a == 1) ([0, 0, 1]:rows)
      right  = minimum $ map (\[x, y, a] -> x) $ filter (\[x, y, a] -> a == 2) ([w, 0, 2]:rows)
      bottom = maximum $ map (\[x, y, a] -> y) $ filter (\[x, y, a] -> a == 3) ([0, 0, 3]:rows)
      top    = minimum $ map (\[x, y, a] -> y) $ filter (\[x, y, a] -> a == 4) ([0, h, 4]:rows)

  print $ if right <= left || top <= bottom
          then 0
          else (right - left) * (top - bottom)
