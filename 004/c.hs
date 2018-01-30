main :: IO ()
main = do
  n <- readLn :: IO Int
  let n' = n `mod` 30
  let initialState = [1, 2, 3, 4, 5, 6]
  let result = loop 0 n' initialState
  putStrLn $ concatMap show result

loop :: Int -> Int -> [Int] -> [Int]
loop i n state
  | i == n = state
  | otherwise = loop (i + 1) n state' where state' = simulate i state

simulate :: Int -> [Int] -> [Int]
simulate i = swapElementsAt i' (i' + 1) where i' = i `mod` 5

swapElementsAt :: Int -> Int -> [a] -> [a]
swapElementsAt a b list = list1 ++ [list !! b] ++ list2 ++ [list !! a] ++ list3
    where   list1 = take a list;
            list2 = drop (succ a) (take b list);
            list3 = drop (succ b) list
