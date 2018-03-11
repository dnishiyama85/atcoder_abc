main :: IO ()
main = do
  [n, a, b] <- (map read . words) <$> getLine :: IO [Int]
  print $ sum $ filter (\i -> let ds = digitSum i 0 in a <= ds && ds <= b) [1..n]

digitSum n carry
  | n < 10 = carry + n
  | otherwise = digitSum (n `div` 10) (carry + n `mod` 10)
