main :: IO ()
main = do
  n <- getLine :: IO String
  putStrLn $ if isSame n then "SAME" else "DIFFERENT"

isSame :: String -> Bool
isSame s = all (\c -> c == head s) s
