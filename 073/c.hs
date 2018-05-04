import Control.Monad
import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- replicateM n readLn :: IO [Int]
  let count = length $ filter odd $ map length $ group $ sort as
  print count
