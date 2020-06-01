import Text.Printf

main = do
    m <- readLn :: IO Int
    putStrLn $ printf "%02d" (solve m)

solve m
    | m <    100 = 0
    | m <=  5000 = m * 10 `div` 1000
    | m <= 30000 = m `div` 1000 + 50
    | m <= 70000 = (m `div` 1000 - 30) `div` 5 + 80
    | m >  70000 = 89
