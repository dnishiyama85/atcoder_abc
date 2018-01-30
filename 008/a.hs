main = do
    [s, t] <- (map read . words) <$> getLine
    putStrLn $ show (t - s + 1)

