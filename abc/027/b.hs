import Debug.Trace
import Text.Printf
import Data.List

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  if sum as `mod` n /= 0
    then putStrLn "-1"
    else print $ solve as (sum as `div` n) n

solve :: [Int] -> Int -> Int -> Int
solve as p n =
  foldl' (\total i -> if needBridge i as p then total + 1 else total)
        0 [0..n-2]

-- i と i + 1 の間に橋をかけるべきか？
needBridge :: Int -> [Int] -> Int -> Bool
needBridge i as p =
  let part = take (i + 1) as
      left = sum part
  in left /= p * (i + 1)
