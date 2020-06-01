main :: IO ()
main = do
  [x, t] <- (map read . words) <$> getLine :: IO [Int]
  print $ max (x - t) 0
