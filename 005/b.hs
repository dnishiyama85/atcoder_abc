import Control.Monad

main = do
    n <- readLn :: IO Int
    ts <- replicateM n readLn :: IO [Int]
    putStrLn $ show $ minimum ts

