main :: IO ()
main = do
  x <- readLn :: IO Int
  a <- readLn :: IO Int
  b <- readLn :: IO Int

  print $ x - a - ((x - a) `div` b) * b
