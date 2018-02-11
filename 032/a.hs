import Control.Monad

main :: IO ()
main = do
  [a, b, n] <- replicateM 3 readLn :: IO [Int]
  let l = lcm a b
      m | n <= l = 1
        | n `mod` l == 0 = n `div` l
        | otherwise = n `div` l + 1
  print $ m * l
