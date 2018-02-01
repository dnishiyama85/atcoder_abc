import Data.List

main :: IO ()
main = do
  [l1, l2, l3] <- sort . map read . words <$> getLine :: IO [Int]
  print $ if l1 == l2 then l3 else l1
