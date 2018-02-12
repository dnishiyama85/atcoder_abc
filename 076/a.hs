main :: IO ()
main = do
  r <- readLn :: IO Int
  g <- readLn :: IO Int
  print $ 2 * g - r
