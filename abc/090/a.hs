main :: IO ()
main = do
  r1 <- getLine
  r2 <- getLine
  r3 <- getLine
  putStrLn [r1!!0 , r2!!1, r3!!2]
