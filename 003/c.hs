import Data.List

main :: IO ()
main = do
  [_, k] <- (map read . words) <$> getLine :: IO [Int]
  rs <- (sortBy (flip compare) . map read . words) <$> getLine :: IO [Float]
  let toWatch =reverse $ take k rs
  let rating = calcRating toWatch
  print rating

calcRating :: [Float] -> Float
calcRating toWatch = foldl (\rating w -> (rating + w) / 2) 0 toWatch
