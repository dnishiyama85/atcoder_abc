main :: IO ()
main = do
  s <- getLine
  print $ length $ filter (== '1') s
