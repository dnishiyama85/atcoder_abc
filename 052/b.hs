import Data.IORef
import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- getLine
  mxRef <- newIORef 0
  xRef <- newIORef 0
  forM_ s $ \c -> do
    mx <- readIORef mxRef
    if c == 'I'
      then modifyIORef xRef (+ 1)
      else modifyIORef xRef (subtract 1)
    x <- readIORef xRef
    writeIORef mxRef $ max mx x

  print =<< readIORef mxRef
