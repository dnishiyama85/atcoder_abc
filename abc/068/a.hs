main :: IO ()
main = ("ABC" ++) <$> getLine >>= putStrLn
