import Control.Monad
import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  rows <- replicateM n $ (parse . words) <$> getLine :: IO [(String, Int)]
  let total = foldl' (\acc (_, p) -> acc + p) 0 rows
      found = find (\(_, p) -> p > total `div` 2) rows

  putStrLn $ case found of
    Nothing -> "atcoder"
    Just (s, _) -> s

parse :: [String] -> (String, Int)
parse [s, p] = (s, read p)
