import Control.Monad
import Data.List

main = do
    n <- readLn :: IO Int
    names <- replicateM n getLine
    putStrLn $ head $ head $
        sortBy (\a b -> compare (length b) (length a) )
        (group $ sort names)

