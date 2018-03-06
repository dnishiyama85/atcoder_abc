{-# LANGUAGE MultiWayIf #-}

import Control.Monad
import Control.Monad.ST
import Data.List
import Data.Array.ST
import Debug.Trace

type Balloon = (Int, Int)

main :: IO ()
main = do
  n <- readLn :: IO Int
  bs <- replicateM n $ (parse . words) <$> getLine :: IO [Balloon]
  print $ binSearch n bs

parse :: [String] -> Balloon
parse [h, s] = (read h, read s)

-- 到達予定時刻順にソート
sortByArrival :: [Balloon] -> Int -> Int -> [Balloon]
sortByArrival balloons n p = binSort n p balloons


-- 高度 p への到達予定時刻
arrival :: Balloon -> Int -> Int
arrival (h, s) p = (p - h) `div` s

-- 得点を p 以下にできるか？
canBeLeq :: Int -> [Balloon] -> Int -> Bool
canBeLeq _ [] _ = True
canBeLeq p sorted@((h, s):bs') t =
  if p < h + s * t
    then False
    else canBeLeq p bs' (t + 1)

-- pで二分探索
binSearch :: Int -> [Balloon] -> Int
binSearch n balloons =
  _binSearch 0 1000000000000000
  where
    _binSearch left right
      | right - left <= 1 = right
      | otherwise =
          let p = (left + right) `div` 2 :: Int
              sorted = sortByArrival balloons n p
          in
            if canBeLeq p sorted 0
              then _binSearch left p
              else _binSearch p right

-- ビンソート
binSort n p balloons = runST $ do
  bins <- newArray (-1, n) [] :: ST s (STArray s Int [Balloon])

  forM_ balloons $ \b -> do
    let time = arrival b p
    if time < 0
      then do
        bin <- readArray bins (-1)
        writeArray bins (-1) (b:bin)
      else if time >= n
        then do
          bin <- readArray bins n
          writeArray bins n (b:bin)
        else do
          bin <- readArray bins time
          writeArray bins time (b:bin)

  concat <$> getElems bins
