import Data.IORef
import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  k <- readLn :: IO Int
  score <- newIORef 1
  replicateM_ n $ do
    now <- readIORef score
    let next = min (now + k) (now * 2)
    writeIORef score next

  print =<< readIORef score
