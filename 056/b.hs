main :: IO ()
main = do
  [w, a, b] <- (map read . words) <$> getLine :: IO [Int]
  print $ if b > a + w
            then b - a - w
            else if a > b + w
              then a - b -w
              else 0
