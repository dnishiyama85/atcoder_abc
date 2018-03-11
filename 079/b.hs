main :: IO ()
main = do
  n <- readLn :: IO Int
  print $ lucas 1 n 1 2

lucas :: Int -> Int -> Int -> Int -> Int
lucas i n l1 l2
  | i >= n = l1
  | otherwise = lucas (i + 1) n (l1 + l2) l1
