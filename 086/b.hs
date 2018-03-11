main :: IO ()
main = do
  [a, b] <-  words <$> getLine :: IO [String]
  let n = read (a ++ b)
  putStrLn $ if isSquare 0 n then "Yes" else "No"

isSquare :: Int -> Int -> Bool
isSquare i n
  | i * i > n = False
  | i * i == n = True
  | otherwise = isSquare (i + 1) n
