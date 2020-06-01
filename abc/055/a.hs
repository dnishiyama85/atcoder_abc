main :: IO ()
main = do
  n <- readLn :: IO Int
  print $ 800 * n - 200 * (n `div` 15)
