import Data.List

main :: IO ()
main = do
  [_n, k] <- (map read . words) <$> getLine :: IO [Int]
  ls <- (sortBy (flip compare) . map read . words) <$> getLine :: IO [Int]
  print $ sum $ take k ls
