import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  k <- readLn :: IO Int
  ps <- (map read . words) <$> getLine :: IO [Int]
  if elem a ps || elem b ps
    then putStrLn "NO"
    else
      if length (nub ps) == length ps
        then putStrLn "YES"
        else putStrLn "NO"
