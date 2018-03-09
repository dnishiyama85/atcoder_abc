main :: IO ()
main = do
  a <- readLn :: IO Integer
  b <- readLn :: IO Integer
  putStrLn $ if a > b
    then "GREATER"
    else if a < b
      then "LESS"
      else "EQUAL"
