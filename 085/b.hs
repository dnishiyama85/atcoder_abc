import Control.Monad
import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  ds <- (sort . nub) <$> replicateM n readLn :: IO [Int]
  print $ length ds
