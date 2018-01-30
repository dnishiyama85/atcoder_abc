main :: IO ()
main = do
  [n, s, t] <- (map read . words) <$> getLine :: IO [Int]
  w <- readLn :: IO Int
  let first = if s <= w && w <= t then 1 else 0
  total <- count first w s t (n - 1)
  print total

count :: Int -> Int -> Int -> Int -> Int -> IO Int
count c _ _ _ 0 = return c
count c w s t n = do
  a <- readLn :: IO Int
  if s <= w + a && w + a <= t
    then count (c + 1) (w + a) s t (n - 1)
    else count c (w + a) s t (n - 1)
