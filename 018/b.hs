import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  s <- getLine
  n <- readLn :: IO Int
  inputs <- replicateM n $ (map read . words) <$> getLine :: IO [[Int]]
  putStrLn $ solve s inputs

solve :: String -> [[Int]] -> String
solve s [] = s
solve s inputs =
  let
      [l, r]:inputs' = inputs
      f = take (l - 1) s
      m = substring (l - 1) (r - l + 1) s
      e = drop r s
  in
    solve (f ++ reverse m ++ e) inputs'

substring :: Int -> Int -> String -> String
substring n m s = take m $ drop n s
