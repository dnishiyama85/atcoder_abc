main :: IO ()
main = do
  n <- readLn :: IO Int
  a <- readLn :: IO Int
  print $ n * n - a
