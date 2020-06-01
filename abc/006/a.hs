import Data.List
import Debug.Trace

main = do
    str_n <- getLine
    let n = read str_n :: Int
    putStrLn $ if (isInfixOf "3" str_n) || (n `mod` 3 == 0) then "YES" else "NO"

