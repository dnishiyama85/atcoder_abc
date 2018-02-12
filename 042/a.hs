import Data.List

main :: IO ()
main = do
  ds <- (sort . map read . words) <$> getLine :: IO [Int]
  putStrLn $ if ds == [5, 5, 7] then "YES" else "NO"
