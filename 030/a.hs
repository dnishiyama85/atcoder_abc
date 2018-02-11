main :: IO ()
main = do
  [a, b, c, d] <- (map read . words) <$> getLine :: IO [Float]
  putStrLn $ if b / a > d / c
    then "TAKAHASHI"
    else if b / a < d / c then "AOKI" else "DRAW"
