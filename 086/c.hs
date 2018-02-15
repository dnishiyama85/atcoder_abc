import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  n <- readLn :: IO Int
  rows <- replicateM n $ (map read . words) <$> getLine :: IO [[Int]]
  putStrLn $ if solve (0, 0, 0) rows then "Yes" else "No"


solve :: (Int, Int, Int) -> [[Int]] -> Bool
solve _ [] = True
solve (x0, y0, t0) ([t, x, y]:rows) =
  let d = abs (x0 - x) + abs (y0 - y)
      dt = t - t0
      c = (d < dt && (dt - d) `mod` 2 == 0)
  in (d == dt || c) && solve (x, y, t) rows
