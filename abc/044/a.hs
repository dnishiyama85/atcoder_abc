import Control.Monad

main :: IO ()
main = do
  [n, k, x, y] <- replicateM 4 readLn :: IO [Int]
  print $ (min n k) * x + (max 0 (n - k)) * y
