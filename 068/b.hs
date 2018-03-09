import Data.List
import Data.Function

main :: IO ()
main = do
  n <- readLn :: IO Int
  print $ fst $ maximumBy (compare `on` snd) $ map (\i -> (i, tryDiv2 i 0) :: (Int, Int)) [1..n]

tryDiv2 :: Int -> Int -> Int
tryDiv2 n cnt
  | n `mod` 2 /= 0 = cnt
  | otherwise = tryDiv2 (n `div` 2) (cnt + 1)
