main :: IO ()
main = do
  s' <- getLine
  t <- getLine
  putStrLn $ restore s' t

restore :: String -> String -> String
restore s' t =
  _restoreLoop (length s' - length t)
  where
    _restoreLoop :: Int -> String
    _restoreLoop start
      | start < 0 = "UNRESTORABLE"
      | otherwise = if isContained s' t start
                      then
                        let s'' = take start s' ++ t ++ drop (start + length t) s'
                        in map (replace 'a') s''
                      else
                        _restoreLoop (start - 1)

isContained :: String -> String -> Int -> Bool
isContained s' t start =
  all (\i -> t!!i == s'!!(start + i) || s'!!(start + i) == '?') [0..length t　- 1]

replace :: Char -> Char -> Char
replace c '?' = c
replace _ c0 = c0
