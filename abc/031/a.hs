main :: IO ()
main = do
  [a, d] <- (map read . words) <$> getLine :: IO [Int]
  print $ if a > d
            then a * (d + 1)
            else (a + 1) * d
