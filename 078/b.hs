main :: IO ()
main = do
  [x, y, z] <- (map read . words) <$> getLine :: IO [Int]
  print $ search 1 x y z

search i x y z
  | (i + 1) * y + (i + 2) * z > x = i
  | otherwise = search (i + 1) x y z
