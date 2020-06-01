import Control.Monad
import Debug.Trace
import Data.List
import Data.Function (on)

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  inputs <- replicateM m $ (parse . words) <$> getLine :: IO [(Int, Int)]
  let result = sortBy (compare `on` fst) $ reduce [(id, concat [friendsOf fid inputs | fid <- friendsOf id inputs]) | id <- [1..n]] inputs
  forM_ result (print . length . snd)


parse :: [String] -> (Int, Int)
parse (a:b:_) = (read a, read b)
parse _ = error "ここに来ることはない"

friendsOf :: Int -> [(Int, Int)] -> [Int]
friendsOf id ls = l1 ++ l2
  where l1 = map snd $ filter (\(myId, _fId) -> id == myId) ls
        l2 = map fst $ filter (\(_myId, fId) -> id == fId) ls

reduce :: [(Int, [Int])] -> [(Int, Int)] -> [(Int, [Int])]
reduce ls inputs = map (\(myId, friendIds) ->
  let reducedIds =(nub $ filter (/= myId) friendIds) \\ friendsOf myId inputs
  in (myId, reducedIds)) ls
