import Debug.Trace
import Data.List

main :: IO ()
main = do
  [n, k] <- (map read . words) <$> getLine :: IO [Int]
  print $ sum $ map (\b -> (subtotal n k b)) [k + 1 .. n]

subtotal n k b =
  let low = (n - (b - 1)) `div` b
      high = (n - k) `div` b
      d = if k == 0 then 1 else 0
  in
    if low < high
      then
        let m = low * b + b
        in
          (low + 1) * (m - (n - (b - 1))) + (high + 1) * (n - k - m + 1) - d
      else (low + 1) * (b - k) - d
