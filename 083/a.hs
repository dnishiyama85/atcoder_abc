main :: IO ()
main = do
  [a, b, c, d] <- (map read . words) <$> getLine :: IO [Int]
  let [l, r] = [a + b, c + d]
  putStrLn $ if l > r then "Left" else if l < r then "Right" else "Balanced"
