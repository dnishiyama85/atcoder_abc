main :: IO ()
main = do
  a <- readLn :: IO Int
  b <- readLn :: IO Int
  h <- readLn :: IO Int
  print $ (a + b) * h `div` 2
