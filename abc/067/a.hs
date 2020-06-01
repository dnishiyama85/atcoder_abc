main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if any (\x -> x `mod` 3 == 0) [a, b, a + b] then "Possible" else "Impossible"
