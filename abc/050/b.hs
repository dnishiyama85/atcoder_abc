import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  ts <- (map read . words) <$> getLine :: IO [Int]
  m <- readLn :: IO Int
  pxs <- replicateM m $ (map read . words) <$> getLine :: IO [[Int]]

  let total = sum ts
  forM_ pxs $ \[p, x] ->
    print $ total - (ts!!(p - 1) - x)
