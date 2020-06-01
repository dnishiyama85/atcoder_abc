import qualified Data.Map as Map

main :: IO ()
main = do
  s <- getLine
  let m = Map.empty :: Map.Map Char Int
      counts = map (show . find (count s m)) "ABCDEF"
  putStrLn $ unwords counts

count :: String -> Map.Map Char Int -> Map.Map Char Int
count "" m = m
count s m =
  let c:s' = s
      m' = Map.insertWithKey (\_ newV oldV -> newV + oldV) c 1 m
  in count s' m'

find :: Map.Map Char Int -> Char -> Int
find m k = Map.findWithDefault 0 k m
