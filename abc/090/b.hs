main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  print $ length $ filter id $ map (\n -> show n == reverse (show n)) [a..b]
