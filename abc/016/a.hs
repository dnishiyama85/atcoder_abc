import Control.Monad

main = do
    [m, d] <- (map read . words) <$> getLine :: IO [Int]
    let divides = m `mod` d == 0
    putStrLn $ if divides then "YES" else "NO"
