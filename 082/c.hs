import Data.List
import Debug.Trace

main :: IO ()
main = do
  _ <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  print $ solve $ format as

format :: [Int] -> [(Int, Int)]
format as =
  map (\bs -> (head bs, length bs)) $ (group . sort) as

solve :: [(Int, Int)] -> Int
solve as = sum $ map (\(b, cnt) ->
 if b > cnt
 then cnt
 else
   if b == cnt
   then 0
   else cnt - b) as

mytrace a = trace (show a) a
