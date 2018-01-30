main = do
    n <- readLn
    putStrLn . show $ solve n

solve :: Int -> Int
solve 12 = 1
solve n = n + 1

