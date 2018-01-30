import qualified Data.Map as Map
dict :: Map.Map Int Int
dict = Map.fromList [(1, 0), (2, 1), (3, 0), (4, 1), (5, 2), (6, 3), (7, 0), (8, 1), (9, 0)]
convert f =  case Map.lookup f dict of
                Just n -> n
main = do
    _ <- readLn :: IO Int
    fs <- (map read . words) <$> getLine :: IO [Int]
    let ans = sum $ map convert fs
    putStrLn $ show ans

