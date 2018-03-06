import Data.List
import Data.Array.IO
import Debug.Trace
import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- (sort . map read . words) <$> getLine :: IO [Int]
  _bs <- (sort . map read . words) <$> getLine :: IO [Int]
  _cs <- (sort . map read . words) <$> getLine :: IO [Int]
  bs <- newListArray (0, n - 1) _bs :: IO (IOUArray Int Int)
  cs <- newListArray (0, n - 1) _cs :: IO (IOUArray Int Int)
  print =<< getElems cs
  print =<< solve as bs cs

solve :: [Int] -> IOUArray Int Int -> IOUArray Int Int -> IO Int
solve as bs cs =
  sum <$> mapM (\a -> solveA a bs cs) as

solveA :: Int -> IOUArray Int Int -> IOUArray Int Int -> IO Int
solveA a bs cs = do
  (s, e) <- getBounds cs
  p <- binSearch a bs s e
  bs' <- drop p <$> getElems bs
  sum <$> mapM (\b -> solveB b cs) bs'

solveB :: Int -> IOUArray Int Int -> IO Int
solveB b cs = do
    (s, e) <- getBounds cs
    p <- binSearch b cs s e
    return (e - p + 1)

binSearch :: Int -> IOUArray Int Int -> Int -> Int -> IO Int
binSearch a bs left right = do
  leftValue <- readArray bs left
  rightValue <- readArray bs right
  (_, e) <- getBounds bs
  if left == 0 && a < leftValue
    then return 0
    else
      if right == e && a >= rightValue
        then return (e + 1)
        else
          if left + 1 >= right
            then return right
            else do
              let p = (left + right) `div` 2
              v <- readArray bs p
              if v <= a
                then binSearch a bs p right
                else binSearch a bs left p
