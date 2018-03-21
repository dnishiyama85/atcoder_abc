{-# LANGUAGE MultiWayIf #-}
main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  print $ if
          | n== 2 || m == 2 -> 0
          | n == 1 && m == 1 -> 1
          | n == 1 -> m - 2
          | m == 1 -> n - 2
          | otherwise -> (n - 2) * (m - 2)
