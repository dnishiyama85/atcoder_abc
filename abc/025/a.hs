import Data.List

main :: IO ()
main = do
  s <- getLine
  n <- readLn :: IO Int
  putStrLn $ sort [[c1, c2] | c1 <- s, c2 <- s] !! (n - 1)
