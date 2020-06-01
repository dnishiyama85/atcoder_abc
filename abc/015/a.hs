main = do
    a <- getLine
    b <- getLine
    let c = if length(a) > length(b) then a else b
    putStrLn c

