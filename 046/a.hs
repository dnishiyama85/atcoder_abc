import Data.List

main :: IO ()
main = do
  as <- (map read . words) <$> getLine :: IO [Int]
  print $ length $ nub as
