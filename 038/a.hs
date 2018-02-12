main :: IO ()
main = do
  s <- getLine
  let lastChar = last s
  putStrLn $ if lastChar == 'T' then "YES" else "NO"
