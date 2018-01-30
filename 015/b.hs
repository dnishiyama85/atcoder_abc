main = do
    n <- readLn :: IO Int
    bs <- (map read . words) <$> getLine :: IO [Int]
    let bs' = filter ( > 0) bs
    let avg = (fromIntegral $ sum bs') / (fromIntegral $ length bs')
    putStrLn $ show $ ceiling avg


