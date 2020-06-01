main :: IO ()
main = do
  [n, m, x] <- (map read . words) <$> getLine :: IO [Int]
  as <- (map read . words) <$> getLine :: IO [Int]
  let c1 = length $ filter (\a -> a <= x) as
  let c2 = length $ filter (\a -> a >= x) as
  print $ min c1 c2
