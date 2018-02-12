main :: IO ()
main = do
  [x, y] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if x < y then "Better" else "Worse"
