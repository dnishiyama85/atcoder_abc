import Data.Array.IO
import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  arr <- newArray (1, n) 0 :: IO (IOArray Int Int)
  forM_ [1..n] $ \i -> do
    a <- readLn :: IO Int
    writeArray arr i a

  cnt <- loop 1 0 n arr
  print cnt

loop :: Int -> Int -> Int -> IOArray Int Int -> IO Int
loop 2 cnt _ _ = return cnt
loop i cnt n arr
  | cnt == n + 1 = return (-1)
  | otherwise = do
      a <- readArray arr i
      loop a (cnt + 1) n arr
