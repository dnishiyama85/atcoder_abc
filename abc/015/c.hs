import Control.Monad
import Data.List
import Data.Bits
import Data.Int
import Debug.Trace

main :: IO ()
main = do
  [n, k] <- (map read . words) <$> getLine :: IO [Int]
  questions <- replicateM n $ map read . words <$> getLine :: IO [[Int8]]
  putStrLn $ if dfs questions [] then "Found" else "Nothing"

dfs :: [[Int8]] -> [Int8] -> Bool
dfs [] answers = judge answers
dfs (ops:questions) answers =
  any (\op -> dfs questions (op:answers)) ops


judge :: [Int8] -> Bool
judge answers = foldl' xor 0 answers == 0
