import Control.Monad

main :: IO ()
main = do
  [n, t] <- (map read . words) <$> getLine :: IO [Int]
  as <- replicateM n readLn :: IO [Int]
  print $ solve 0 0 0 as t

solve :: Int -> Int -> Int -> [Int] -> Int -> Int
-- nextClose : 次にドアが閉まる予定の時刻
-- lastOpen : 最後にドアが空いた時刻
solve total lastOpen nextClose [] _ = total + nextClose - lastOpen
solve total lastOpen nextClose as t =
  let a:as' = as -- 今回の客が来た時刻
  in
    if nextClose < a
      -- ドアはいったん閉まった
      then solve  (total + nextClose - lastOpen) a (a + t) as' t
      -- 開き時間延長
      else solve total lastOpen (a + t) as' t
