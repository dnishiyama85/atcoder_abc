import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  n <- readLn :: IO Int
  ngs <- replicateM 3 readLn :: IO [Int]
  putStrLn $ if solve n ngs 0 then "YES" else "NO"

solve :: Int -> [Int] -> Int -> Bool
solve n ngs 100 = False
solve n ngs count
  | n `elem` ngs = False -- いきなりNGの場合
  | n <= 3 = True -- カウントを1以上残して、いま 1, 2, 3 なら ゴール可能
  | n - 3 `notElem` ngs =
      -- 3 行けるときは行く
      solve (n - 3) ngs (count + 1)
  | n - 2 `notElem` ngs =
      -- 3 行けないので2いけるなら行く
      solve (n - 2) ngs (count + 1)
  | n - 1 `notElem` ngs =
     -- 2も行けないとき、1行けるなら行く
     solve (n - 1) ngs (count + 1)
  | otherwise = False -- 1, 2, 3 どれを選んでもng
