import Data.Char
main = do
    [c] <- getLine
    putStrLn $ show $ ord(c) - ord('A') + 1
