main :: IO ()
main = do
  n <- getLine
  putStrLn $ if isGoodInteger n then "Yes" else "No"

isGoodInteger :: String -> Bool
isGoodInteger n =
  let h = head n
      t = last n
  in (h == n!!1 && h == n!!2) || (t == n!!1 && t == n!!2)
