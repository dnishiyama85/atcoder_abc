import Control.Monad
import Data.Array.IO

main :: IO ()
main = do
  n <- readLn :: IO Int
  fs <- replicateM n readLn :: IO [Int]
  as <- newArray (0, 100000) False :: IO (IOArray Int Bool)
  count <- check fs as 0
  print count

check :: [Int] -> IOArray Int Bool -> Int -> IO Int
check [] _ count = return count
check fs as count = do
  let f:fs' = fs
  visited <- readArray as f
  writeArray as f True
  if visited
    then check fs' as (count +1)
    else check fs' as count
