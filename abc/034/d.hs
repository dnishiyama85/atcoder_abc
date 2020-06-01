import Control.Monad
import Data.List
import Debug.Trace

main :: IO ()
main = do
  [n, k] <- (map read . words) <$> getLine :: IO [Int]
  rows <- replicateM n $ parse <$> getLine :: IO [(Int, Int)]
  print $ searchMaxConcentration rows k

-- 濃度 d で二分探索
searchMaxConcentration :: [(Int, Int)] -> Int -> Float
searchMaxConcentration rows k =
  _binSearch 0.0 100.0 0
  where
    _binSearch :: Float -> Float -> Int -> Float
    _binSearch left _ 100 = left
    _binSearch left right count =
      let center = (left + right) / 2
      in if canBeConcentrationHigherThan rows center k
           then _binSearch center right (count + 1)
           else _binSearch left center (count + 1)

-- 濃度 d 以上にできるか？
canBeConcentrationHigherThan :: [(Int, Int)] -> Float -> Int -> Bool
canBeConcentrationHigherThan rows d k =
  let ret = greedy rows d k >= 0
  in ret

-- 濃度 d と個数 k を与えて、Σ(pw - dw) の大きいものから貪欲に k 個取って和を計算
greedy :: [(Int, Int)] -> Float -> Int -> Float
greedy rows d k =
  let sortedAmounts = sortBy (flip compare) $ map (\(w, p) -> amount p w) rows
  in sum $ take k sortedAmounts
  where
    amount :: Int -> Int -> Float
    amount p w = fromIntegral p * fromIntegral w - d * fromIntegral w


parse :: String -> (Int, Int)
parse line =
  let [w, p] = (map read . words) line
  in (w, p)
