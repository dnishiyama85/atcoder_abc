main :: IO ()
main = do
  n <- getLine
  putStrLn $ if n == reverse n then "Yes" else "No"
