main = do
    [x, y] <- (map read . words) <$> getLine :: IO [Int]
    putStrLn $ show $ max x y

