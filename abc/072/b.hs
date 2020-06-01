import Control.Monad.ST
import Data.STRef
import Data.Array.ST
import Control.Monad

main :: IO ()
main = do
  s <- getLine
  putStrLn $ oddString s

oddString :: String -> String
oddString str = runST $ do
  oddStr <- newSTRef ""
  arrStr <- newListArray (0, length str - 1) str :: ST s (STUArray s Int Char)
  forM_ [0..length str - 1] $ \i ->
    if i `mod` 2 == 1
      then return ()
      else do
        c <- readArray arrStr i
        now <- readSTRef oddStr
        writeSTRef oddStr (c:now)

  reverse <$> readSTRef oddStr
