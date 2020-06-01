import Control.Monad
import Control.Monad.ST
import Data.STRef
import Debug.Trace

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- getLine :: IO String
  print $ if isAccessory s
          then (n - 1) `div` 2
          else -1

isAccessory :: String -> Bool
isAccessory s
  | length s `mod` 2 == 0 = False
  | otherwise = s == genAccessory (length s)

genAccessory :: Int -> String
genAccessory len = runST $ do
  acc <- newSTRef "b"
  forM_ [1..(len - 1) `div` 2] $ \i -> do
    let (l, r) = case i `mod` 3 of
              0 -> ("b", "b")
              1 -> ("a", "c")
              2 -> ("c", "a")
              _ -> error "ここに来ることはない"
    s <- readSTRef acc
    writeSTRef acc (l ++ s ++ r)

  readSTRef acc
