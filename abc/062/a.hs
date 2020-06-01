data Group = G0 | G1 | G2 deriving Eq

grouping :: [[Int]]
grouping = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]]

main :: IO ()
main = do
  [x, y] <- (map read . words) <$> getLine :: IO [Int]
  putStrLn $ if findGroup x == findGroup y then "Yes" else "No"

findGroup :: Int -> Group
findGroup x
  | x `elem` grouping!!0 = G0
  | x `elem` grouping!!1 = G1
  | x `elem` grouping!!2 = G2
  | otherwise = error "ここに来ることはない"
