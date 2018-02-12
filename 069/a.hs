main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  print $ (n - 1) * (m - 1)
