main :: IO ()
main = do
  [r, g, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ let col = r * 100 + g * 10 + b
   in if col `mod` 4 == 0 then "YES" else "NO"
