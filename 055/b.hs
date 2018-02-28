import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Integer
  let result = foldl' (\acc i -> acc * i `mod` 1000000007) 1 [1..n]
  print result
