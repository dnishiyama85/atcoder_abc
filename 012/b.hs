import Text.Printf

main = do
    n <- readLn :: IO Int
    putStrLn $ printf "%02d:%02d:%02d" (n `div` 3600) (n `div` 60 `mod` 60) (n `mod` 60)

