main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if a * b `mod` 2 == 0 then "Even" else "Odd"
