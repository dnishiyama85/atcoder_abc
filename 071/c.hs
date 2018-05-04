{-# LANGUAGE MultiWayIf #-}

import Data.List

main :: IO ()
main = do
  _n <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  let d = filter (\(_e, l) -> l > 1) $ map (\e -> (head e, length e)) $ group $ sortBy (flip compare) as
  print $ if
            | null d -> 0 :: Int
            | length d >= 1 && snd(head d) >= 4 -> fst(head d) * fst(head d)
            | length d >= 2 -> fst(head d) * fst(d!!1)
