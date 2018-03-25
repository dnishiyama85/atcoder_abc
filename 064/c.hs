import Data.Array.IO

main :: IO ()
main = do
  [n, x] <- (map read . words) <$> getLine :: IO [Int]
  as <- (map read . words) <$> getLine :: IO [Int]
  asArr <- newListArray (0, n - 1) as :: IO (IOArray Int Int)
  print =<< solve asArr 1 n x 0

solve :: IOArray Int Int -> Int -> Int -> Int -> Int -> IO Int
solve asArr ptr n x cnt
  | ptr == n = return cnt
  | otherwise = do
      a0 <- readArray asArr (ptr - 1)
      a1 <- readArray asArr ptr
      cnt' <-
        if a0 + a1 <= x
          then return cnt
          else do
            let toEat = (a0 + a1 - x)
            if a1 >= toEat
              then writeArray asArr ptr (a1 - toEat)
              else do
                writeArray asArr ptr 0
                writeArray asArr (ptr - 1) (a0 - (toEat - a1))
                
            return (cnt + toEat)

      solve asArr (ptr + 1) n x cnt'
