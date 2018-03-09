import Control.Monad

main :: IO ()
main = do
  [h, w] <- (map read . words) <$> getLine :: IO [Int]
  replicateM_ (w + 2) $ putStr "#"
  putStrLn ""
  replicateM_ h $ do
    putStr "#"
    getLine >>= putStr
    putStrLn "#"

  replicateM_ (w + 2) $ putStr "#"
  putStrLn ""
