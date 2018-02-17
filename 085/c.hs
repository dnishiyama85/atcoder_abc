main :: IO ()
main = do
  [n, yen] <- (map read . words) <$> getLine :: IO [Int]
  let candidates = [(x, y, n - x - y) | x <- [0..n], y <- [0..n - x],
                                        10000 * x + 5000 * y + 1000 * (n - x - y) == yen]
  if null candidates
    then putStrLn "-1 -1 -1"
    else do
      let (a, b, c) = head candidates
      putStrLn $ show a ++ " " ++ show b ++ " " ++ show c
