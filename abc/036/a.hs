main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  print $ (b + a - 1) `div` a 
