import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  k <- readLn :: IO Int
  xs <- (map read . words) <$> getLine :: IO [Int]
  print $ 2 * foldl' (\acc x -> acc + min x (k - x)) 0 xs
