main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  -- すべてのケースに正解する確率の逆数
  let pPass = 2^m
  -- すべてのケースが終了するまでにかかる時間
      l = 1900 * m + 100 * (n - m)
  print $ pPass * l
