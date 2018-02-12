main :: IO ()
main = do
  [a, b] <- (map (parse . read) . words) <$> getLine :: IO [Int]
  putStrLn $ if a > b then "Alice" else
             if a < b then "Bob"
             else "Draw"

parse :: Int -> Int
parse 1 = 14
parse n = n
