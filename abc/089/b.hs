import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- concat . words <$> getLine :: IO String
  let len = length $ nub s
  putStrLn $ if len == 4
          then "Four" else "Three"
