import Control.Monad
import Control.Applicative
import Data.List

main = do
    n <- readLn :: IO Int
    as <- replicateM n readLn :: IO [Int]
    putStrLn $ show ((nub . reverse . sort) as !! 1)

