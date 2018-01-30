import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  print n
  replicateM_ n $ putStrLn "1"
