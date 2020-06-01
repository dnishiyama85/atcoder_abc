main :: IO ()
main = do
  n <- readLn :: IO Int
  print $ search 1 n

search :: Int -> Int -> Int
search i n
  | (i + 1)^2 > n = i^2
  | otherwise = search (i + 1) n
