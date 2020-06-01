main :: IO ()
main = do
  s <- getLine
  putStrLn $ solve s "abcdefghijklmnopqrstuvwxyz"

solve s cs
  | null cs = "None"
  | otherwise =
    let c:cs' = cs
    in
      if elem c s then solve s cs' else [c]
