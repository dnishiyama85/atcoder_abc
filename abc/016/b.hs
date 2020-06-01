main = do
    [a, b, c] <- (map read . words) <$> getLine :: IO [Int]
    let (x, y) = (a + b == c, a - b == c)
    let ans = case (x, y) of
                (True, True)   -> "?"
                (True, False)  -> "+"
                (False, True)  -> "-"
                (False, False) -> "!"

    putStrLn ans
