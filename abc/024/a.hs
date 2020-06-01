main :: IO ()
main = do
  [a, b, c, k] <- (map read . words) <$> getLine :: IO [Int]
  [s, t] <- (map read . words) <$> getLine :: IO [Int]

  let subTotal = s * a + t * b
      total = if s + t >= k then subTotal - c * (s + t) else subTotal

  print total
