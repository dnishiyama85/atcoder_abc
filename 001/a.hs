main = do
    h1 <- readLn :: IO Int
    h2 <- readLn :: IO Int
    putStrLn $ show (h1 - h2)

