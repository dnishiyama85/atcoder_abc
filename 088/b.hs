import Data.List

main :: IO ()
main = do
  _ <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  let (alice, bob) = oddEven $ sortBy (flip compare) as
  print $ sum alice - sum bob

-- | リストの要素を偶数番目の要素と奇数番目の要素のリストに分ける関数
oddEven :: [Int] -> ([Int], [Int])
oddEven list = halves list [] []
    where
        halves []       oddList evenList = (oddList,evenList)
        halves [x]      oddList evenList = (oddList++[x],evenList)
        halves (x:y:ys) oddList evenList = halves ys (oddList++[x]) (evenList++[y])
