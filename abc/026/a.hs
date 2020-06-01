import Control.Monad.Trans.State

main :: IO ()
main = do
  a <- readLn :: IO Int
  let (m, _) = runState (maxSum a) ([1..a], 0)
  print m

type Hoge = ([Int], Int) -- (残りのx, 今のmax)

maxSum :: Int -> State Hoge Int
maxSum a = do
  (x:xs, m) <- get
  if null xs
  then return m
  else do
    let y = a - x
        m' = max (x * y) m
    put (xs, m')
    maxSum a
