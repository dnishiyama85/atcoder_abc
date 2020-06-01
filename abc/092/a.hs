import Control.Monad

main :: IO ()
main = do
  [a, b, c, d] <- replicateM 4 readLn :: IO [Int]
  print $ min a b + min c d
