import Data.IORef
import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  s <- getLine
  t <- readLn :: IO Int
  (x, y, q) <- solve s
  let d = abs x + abs y
  print $ if t == 1
            then  d + q
            else if d - q < 0
              then (q - d) `mod` 2
              else d - q

solve :: String -> IO (Int, Int, Int)
solve path = do
  pos <- newIORef (0, 0, 0)
  forM_ path $ \c -> do
          (x, y, q) <- readIORef pos
          let newPos =
                case c of
                  'L' -> (x - 1, y, q)
                  'R' -> (x + 1, y, q)
                  'U' -> (x, y + 1, q)
                  'D' -> (x, y - 1, q)
                  '?' -> (x, y, q + 1)
          writeIORef pos newPos

  readIORef pos
