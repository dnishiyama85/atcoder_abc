main :: IO ()
main = do
  q <- readLn :: IO Int
  case q of
    1 -> putStrLn "ABC"
    2 -> putStrLn "chokudai"

  
