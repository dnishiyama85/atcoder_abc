main = do
    n <- readLn :: IO Int
    putStrLn $ show $ (n + 1) `div` 2

