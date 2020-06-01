import Data.List

main :: IO ()
main = do
  as <- (sort .map read . words) <$> getLine :: IO [Int]
  putStrLn $ if as!!0 + as!!1 == as!!2 then "Yes" else "No"
