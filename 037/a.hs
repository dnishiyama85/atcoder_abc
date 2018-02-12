main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
  print $ c `div` min a b
