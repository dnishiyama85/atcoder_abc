import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  [d, x] <- (map read . words) <$> getLine :: IO [Int]
  as <- replicateM n readLn :: IO [Int]
  print $ x + sum (map (\i -> chocolatesFor i as d) [0..n-1])

chocolatesFor :: Int -> [Int] -> Int -> Int
chocolatesFor i as d =
  let a = as !! i
      t = (d - 1) `div` a
  in t + 1
