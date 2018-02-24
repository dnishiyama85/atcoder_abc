import Control.Monad

main :: IO ()
main = do
  [h, w] <- (map read . words) <$> getLine :: IO [Int]
  replicateM_ h $ do
    l <- getLine
    putStrLn l
    putStrLn l
