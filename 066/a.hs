import Data.List

main :: IO ()
main = do
  [a, b, c] <- (sort . map read . words) <$> getLine :: IO [Int]
  print $ a + b
