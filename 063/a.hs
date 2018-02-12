main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ let s = a + b in if s < 10 then show s else "error"
