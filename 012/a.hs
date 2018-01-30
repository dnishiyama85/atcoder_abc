main = do
    cs <- (map read . words) <$> getLine :: IO [Int]
    let [a, b] = cs
    putStrLn $ (show b) ++ " " ++ (show a)

