main :: IO ()
main = getLine >>= putStrLn . (++ "s")
