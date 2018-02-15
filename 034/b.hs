main :: IO ()
main = do
  n <- readLn :: IO Int
  print $ if n `mod` 2 == 0 then n - 1 else n + 1
