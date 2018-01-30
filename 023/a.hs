main = do
  n <- readLn :: IO Int
  print $ n `div` 10 + n `mod` 10
  
