import Control.Monad
import Data.Array.IO

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  counts <- newArray (1, n) 0 :: IO (IOArray Int Int)
  replicateM_ m $ do
    [a, b] <- (map read . words) <$> getLine :: IO [Int]
    incr counts a
    incr counts b

  mapM_ print =<< getElems counts

incr array i = do
  c <- readArray array i
  writeArray array i (c + 1)
