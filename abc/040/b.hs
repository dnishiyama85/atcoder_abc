main :: IO ()
main = do
  n <- readLn :: IO Int
  let a = [ let h = n `div` w in abs(w - h) + (n - w * h) | w <- [1..n]]
  print $ minimum a
