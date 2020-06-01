import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  blues <- replicateM n readLn :: IO [Int]

  m <- readLn :: IO Int
  reds <- replicateM m readLn :: IO [Int]

  
