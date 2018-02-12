main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
  print $ 2 * (a * b + b * c + c * a)
