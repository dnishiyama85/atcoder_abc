main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    let c = if a `mod` b == 0
                then 0
                else b - a `mod` b
    putStrLn $ show c

