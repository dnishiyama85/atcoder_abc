import Control.Monad
import Control.Monad.ST
import Data.Array.ST

main :: IO ()
main = do
  [n, k] <- (map read . words) <$> getLine :: IO [Int]
  nums <- (map read . lines) <$> getContents :: IO [Int]
  print $ syakutori nums n k

syakutori :: [Int] -> Int -> Int -> Int
syakutori nums n k =
  if 0 `elem` nums
    then n
    else runST $ do
      numsArray <- newListArray (0, n) nums :: ST s (STUArray s Int Int)
      _syakutoriLoop numsArray (0, 0, 0, 1)
      where
        _syakutoriLoop :: STUArray s Int Int -> (Int, Int, Int, Int) -> ST s Int
        _syakutoriLoop nArray (left, right, mx, prod) =
          if right >= n
            then return mx
            else do
              r <- readArray nArray right
              let prod' = prod * r
              if prod' <= k
               then _syakutoriLoop nArray (left, right + 1, max mx (right + 1 - left), prod')
               else if left + 1 <= right
                 then do
                   l <- readArray nArray left
                   _syakutoriLoop nArray (left + 1, right, mx, max (prod `div` l) 1)
                 else _syakutoriLoop nArray (left + 1, right + 1, mx, 1)
