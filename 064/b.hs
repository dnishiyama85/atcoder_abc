import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- (sort . map read . words) <$> getLine :: IO [Int]
  print $ last as - head as
