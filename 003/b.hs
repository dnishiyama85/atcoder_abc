import Data.List

main = do
    s <- getLine
    t <- getLine
    putStrLn (if judge s t then "You can win" else "You will lose")

judge :: [Char] -> [Char] -> Bool
judge s t = all id  (zipWith judge_char s t)

judge_char :: Char -> Char -> Bool
judge_char c1 c2
    | c1 == c2 = True
    | c1 == '@' = elem c2 "@atcoder"
    | c2 == '@' = elem c1 "@atcoder"
    | otherwise = False

