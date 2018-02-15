main :: IO ()
main = do
  n <- readLn :: IO Int
  as1 <- (map read . words) <$> getLine :: IO [Int]
  as2 <- (map read . words) <$> getLine :: IO [Int]
  print $ maximum $ map (\i -> sum $ take (i + 1) as1 ++ drop i as2) [0..n]
