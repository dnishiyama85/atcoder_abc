import Control.Monad.Trans.State
import Debug.Trace

type Stack = [Int]

main :: IO ()
main = do
  t  <- readLn :: IO Int
  n  <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  m  <- readLn :: IO Int
  bs <- (map read . words) <$> getLine :: IO [Int]
  let isSuccess = evalState (takoyaki t) (as, bs)
  putStrLn $ if isSuccess then "yes" else "no"

takoyaki :: Int -> State (Stack, Stack) Bool
takoyaki t = do
  (takoyakis, guests) <- trace "aaaaa" <$> get
  if null guests -- お客を全部捌き切った
    then return True
    else
      let
        g:guests' = guests
        (is_ok, takoyakis') = checkTakoyaki t g takoyakis
      in
        do
          put $ trace("takoyakis' = " ++ show takoyakis') (takoyakis', guests')
          if is_ok
            then takoyaki t
            else
              return False

checkTakoyaki :: Int -> Int -> Stack -> (Bool, Stack)
checkTakoyaki _ _ [] = (False, [])
checkTakoyaki t guest takoyakis
  | guest < tako = (False, takoyakis)
  | tako + t < guest = checkTakoyaki t guest takoyakis'
  | otherwise = (True, takoyakis')
  where tako:takoyakis' = takoyakis
