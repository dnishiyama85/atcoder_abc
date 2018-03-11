import Data.Array.IO
import Data.IORef
import Control.Monad

main :: IO ()
main = do
  [h, w] <- (map read . words) <$> getLine
  table <- newListArray (0, h - 1) [] :: IO (IOArray Int (IOArray Int Char))
  forM_ [0..h - 1] $ \i -> do
    row <- newListArray (0, w - 1) =<< getLine :: IO (IOArray Int Char)
    writeArray table i row

  let check (i, j) = 0 <= i && i <= h - 1 && 0 <= j && j <= w - 1
  let incr cnt = modifyIORef cnt (+ 1)

  forM_ [0..h - 1] $ \i -> do
    row <- readArray table i
    forM_ [0..w - 1] $ \j -> do
      cell <- readArray row j
      when (cell == '.') $ do
        count <- newIORef 0
        let dirs = [
                    (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                    (i,     j - 1),             (i,     j + 1),
                    (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                   ]
        forM_ dirs $ \d ->
          when (check d) $ do
            c <- get table d
            when (c == '#') $ incr count

        num <- readIORef count
        writeArray row j $ (head . show) num

  rows <- getElems table
  result <- mapM getElems rows

  forM_ result putStrLn


get arr (i, j) = do
  row <- readArray arr i
  readArray row j
