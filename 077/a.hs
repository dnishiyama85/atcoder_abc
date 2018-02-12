main :: IO ()
main = do
  r1 <- getLine
  r2 <- getLine
  putStrLn $ if r1 == reverse r2 then "YES" else "NO"
