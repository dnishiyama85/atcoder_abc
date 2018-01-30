main = do
    w <- getLine
    putStrLn $ Prelude.foldl (\s c -> remove s c) w ['a', 'i', 'u', 'e', 'o']

remove :: String -> Char -> String
remove s c = filter (\c' -> c /= c') s

