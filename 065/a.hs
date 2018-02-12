main :: IO ()
main = do
  [x, a, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if a - b >= 0 then "delicious" else
    if b - a <= x then "safe" else "dangerous"
