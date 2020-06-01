import Text.Printf
import Data.IORef
import Control.Monad
import Debug.Trace
import Data.Char

mytrace a = trace (show a) a

main :: IO ()
main = do
  [a, b, c, d] <- map digitToInt <$> getLine :: IO [Int]
  results <- newIORef []
  forM_ [1, 2] $ \i -> do
    let op1 = if i == 1 then (+) else (-)
    forM_ [1, 2] $ \j -> do
      let op2 = if j == 1 then (+) else (-)
      forM_ [1, 2] $ \k -> do
        let op3 = if k == 1 then (+) else (-)
        when (op3 (op2 (op1 a b) c) d == 7) $ do
          acc <- readIORef results
          writeIORef results ((i, j, k):acc)

  (i, j, k) <- head <$> readIORef results
  putStrLn $ printf "%d%s%d%s%d%s%d=7" a (opshow i) b (opshow j) c (opshow k) d

opshow :: Int -> String
opshow 1 = "+"
opshow 2 = "-"
