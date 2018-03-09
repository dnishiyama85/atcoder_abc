main :: IO ()
main = do
  s <- getLine
  print $ length $ solve $ deleteLast s

deleteLast s = take (length s - 1) s

solve s =
  if isEvenString s
    then s
    else solve $ deleteLast s

isEvenString s
  | length s `mod` 2 == 1 = False
  | otherwise =
      let len = length s `div` 2
          first = take len s
          second = drop len s
      in
        first == second
