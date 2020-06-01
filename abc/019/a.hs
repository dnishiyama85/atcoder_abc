import Data.List

main :: IO ()
main = do
  [_, b, _] <- (sort . map read . words) <$> getLine :: IO [Int]
  print b
