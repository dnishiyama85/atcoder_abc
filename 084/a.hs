main :: IO ()
main = do
  m <- readLn :: IO Int
  print $ 24 + (24 - m)
