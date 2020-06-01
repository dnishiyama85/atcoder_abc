main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  print $ count as 0

count :: [Int] -> Int -> Int
count as carry
  | all (\a -> a `mod` 2 == 0) as = count (map (`div` 2) as) (carry + 1)
  | otherwise = carry
