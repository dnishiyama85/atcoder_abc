import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  rows <- replicateM n getLine :: IO [String]
  forM_ [0..n-1] $ \i -> do
    forM_ [0..n-1] $ \j ->
      putStr [rows !! (n - j - 1) !! i]
    putStrLn ""
