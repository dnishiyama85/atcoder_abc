import Data.Char
solve (n:ame) = (return $ Data.Char.toUpper n) ++ (map Data.Char.toLower ame)
main = do
    name <- getLine
    putStrLn $ solve name

