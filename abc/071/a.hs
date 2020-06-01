main :: IO ()
main = do
  [x, a, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if abs (x - a) < abs (x - b) then "A" else "B"
