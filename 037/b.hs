import Control.Monad
import Data.Array.IO

main :: IO ()
main = do
  [n, q] <- (map read . words) <$> getLine :: IO [Int]
  rows <- replicateM q $ (map read . words) <$> getLine :: IO [[Int]]
  as <- newArray (1, n) 0 :: IO (IOArray Int Int)
  forM_ rows $ \[l, r, t] ->
    forM_ [l..r] $ \i -> writeArray as i t
  result <- getElems as :: IO [Int]
  forM_ result print
