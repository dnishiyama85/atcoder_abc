main :: IO ()
main = do
  [k, s] <- (map read . words) <$> getLine :: IO [Int]
  print $ length [1 | x <- [0..k], y <- [0..k], 0 <= s - x - y, s - x - y <= k]
