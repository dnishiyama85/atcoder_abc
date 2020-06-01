import Data.Array.IO
import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  n <- readLn :: IO Int
  arr <- newArray (0, 1000001) 0 :: IO (IOUArray Int Int)
  replicateM_ n $ do
     [a, b] <- (map read . words) <$> getLine :: IO [Int]
     writeArray arr a =<< ((1 +) <$> readArray arr a)
     writeArray arr (b + 1) =<< ((-1 + ) <$> readArray arr (b + 1))
  list <- getElems arr :: IO [Int]
  print $ fst $ findMax $ (trace $ show list) list

findMax :: [Int] -> (Int, Int)
findMax = foldl
  (\(m, c) v -> let c' = c + v; m' = max m c' in (m', c')) (0, 0)
