main = do
    [n, x] <- (map read . words) <$> getLine :: IO [Int]
    prices <- (map read . words) <$> getLine :: IO [Int]
    putStrLn $ show $ solve x 0 0 prices

solve 0 bit sum prices = sum
solve x bit sum prices = solve (x `div` 2) (bit + 1) sum' prices
    where sum' = sum + (prices !! bit) * (x `mod` 2)
