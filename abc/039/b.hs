main :: IO ()
main = do
  x <- readLn :: IO Int
  print $ search x 1

search :: Int -> Int -> Int
search x n
  | n^4 == x = n
  | otherwise = search x (n + 1)
