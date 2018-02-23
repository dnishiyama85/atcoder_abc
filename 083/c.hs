main :: IO ()
main = do
  [x, y] <- (map read . words) <$> getLine :: IO [Int]
  print $ solve x y [x]

solve :: Int -> Int -> [Int] -> Int
solve x y acc
  | x * 2 > y = length acc
  | otherwise = solve (x * 2) y (x:acc)
