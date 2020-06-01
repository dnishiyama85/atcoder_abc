import Control.Monad
import Control.Monad.ST
import Data.STRef

main :: IO ()
main = do
  [n, a, b] <- (map read . words) <$> getLine :: IO [Int]
  inputs <- replicateM n $ parse . words <$> getLine :: IO [(String, Int)]
  let result = solve inputs a b
  putStrLn $ if result > 0 then "East " ++ show result
             else if result == 0 then "0"
             else "West " ++ show (- result)


parse :: [String] -> (String, Int)
parse row = (s, read d) where [s, d] = row

solve :: [(String, Int)] -> Int -> Int -> Int
solve inputs a b = runST $ do
  pos <- newSTRef 0
  forM_ inputs $ \(s, d) ->
    let move = max a (min d b)
    in
      case s of
        "West" -> modifySTRef pos (+ (-move))
        "East" -> modifySTRef pos (+ move)
        _      -> error "ここに来ることはない"

  readSTRef pos
