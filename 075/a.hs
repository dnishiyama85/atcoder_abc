main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
  print $ if a == b then c else
    if a == c then b else a
