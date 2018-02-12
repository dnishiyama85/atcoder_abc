main :: IO ()
main = do
  [w, h] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if 4 * h == 3 * w then "4:3" else "16:9"
  
