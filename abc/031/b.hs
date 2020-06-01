import Control.Monad

main :: IO ()
main = do
  [l, h] <- (map read . words) <$> getLine :: IO [Int]
  n <- readLn :: IO Int
  as <- replicateM n readLn :: IO [Int]
  let result = map (\a -> if a > h then -1 else if a >= l then 0 else l - a) as
  forM_ result print
