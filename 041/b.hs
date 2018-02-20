{-# LANGUAGE NumDecimals #-}
main :: IO ()
main = do
  [a, b, c] <- (map read . words) <$> getLine :: IO [Integer]
  print $ a * b * c `mod` (1e9 + 7)
