main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if any (\n -> n * a `mod` b == c) [1..b]
               then "YES"
               else "NO"
