main :: IO ()
main = do
  a <- readLn :: IO Int
  b <- readLn :: IO Int
  c <- readLn :: IO Int
  x <- readLn :: IO Int
  print $ length [True | i <- [0..a], j <- [0..b], k <- [0..c], 500 * i + 100 * j + 50 * k == x]
