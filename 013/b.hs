main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    let c = if a > b
                then
                  min (a - b) (b + 10 - a)
                else
                  min (b - a) (a + 10 - b)
    putStrLn $ show c

