main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if b - a == c - b then "YES" else "NO"
