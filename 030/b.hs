import Data.List

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Float]
  let t = if n < 12 then n else n - 12
      short = (t + m / 60) * 30 -- 短針
      long = m * 6 -- 長針
      [l, h] = sort [short, long]
  print $ min (h - l) (l - h + 360)
