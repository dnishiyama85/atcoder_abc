main :: IO ()
main = do
  [a, b, c, d] <- (map read . words) <$> getLine :: IO [Int]
  print $ max (a * b) (c * d)
