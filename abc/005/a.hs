main = do
    [x, y] <- (map read . words) <$> getLine :: IO [Int]
    putStrLn $ show (y `div` x)

