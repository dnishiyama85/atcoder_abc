{-# LANGUAGE MultiWayIf #-}
main :: IO ()
main = do
  [a, b, c, d] <- (map read . words) <$> getLine :: IO [Int]
  print $ if
    | b < c                      -> 0
    | a <= c && c <= b && b <= d -> b - c
    | c <= a && a <= d && d <= b -> d - a
    | c <= a && b <= d           -> b - a
    | a <= c && d <= b           -> d - c
    | d < a                      -> 0
    | otherwise                  -> 0
