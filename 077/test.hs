import Debug.Trace

binSearch a bs left right
  | left == 0 && a < bs !! left = 0
  | left + 1 >= right = right
  | otherwise =
    let p = (left + right) `div` 2
        v = bs !! p
    in trace ("left = " ++ show left ++ ", right = " ++ show right ++ ", a = " ++ show a　++ ", p = " ++ show p ++ ", v = " ++ show v ++ ", bs = " ++ show bs) $ if v <= a then binSearch a bs p right else binSearch a bs left p

bs = [6,9,58,79,84,323]

main :: IO ()
main = do
  a <- readLn :: IO Int
  print $ binSearch a bs 0 5
