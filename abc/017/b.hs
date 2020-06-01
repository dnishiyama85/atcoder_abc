main :: IO ()
main = do
  s <- reverse <$> getLine
  putStrLn $ if isReversedChokuWord s then "YES" else "NO"

isReversedChokuWord :: String -> Bool
isReversedChokuWord "" = True
isReversedChokuWord (h:t)
  | (h == 'o' || h == 'k' || h == 'u') && isReversedChokuWord t = True
  | h == 'h' =
       t /= "" &&
        (let c:t' = t in c == 'c' && isReversedChokuWord t')
  | otherwise = False
