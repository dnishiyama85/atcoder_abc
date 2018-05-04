import Control.Monad
import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  ts <- replicateM n readLn :: IO [Int]
  print $ foldl' lcm 1 ts
