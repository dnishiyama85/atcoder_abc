import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  rows <- replicateM n $ (map read . words) <$> getLine :: IO [[Int]]
  print =<< foldM (\acc [l, r] -> return (acc + r - l + 1)) 0 rows
