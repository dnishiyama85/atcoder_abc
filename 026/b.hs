import Data.List
import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  n <- readLn :: IO Int
  (r:rs) <- sortBy (flip compare) <$> (replicateM n $ read <$> getLine :: IO [Int]) :: IO [Int]
  let reds = oddElements (diffSeq rs [] (fromIntegral r)) []
  print $ sum $ map (\(inner, outer) -> pi * (outer * outer - inner * inner)) $ reds

-- 内径と外径のペア
diffSeq :: [Int] -> [(Float, Float)] -> Int -> [(Float, Float)]
diffSeq [] result outer  = reverse $ (0.0, fromIntegral outer):result
diffSeq (inner:xs) result outer = diffSeq xs ((fromIntegral inner, fromIntegral outer):result) inner

-- 奇数番目の要素を取る
oddElements :: [(Float, Float)] -> [(Float, Float)] -> [(Float, Float)]
oddElements [] acc = acc
oddElements [o] acc = o:acc
oddElements (o:_e:xs) acc = oddElements xs (o:acc)
