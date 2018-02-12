main :: IO ()
main = do
  [x, y] <- (map convert . words) <$> getLine
  putStrLn $ if x < y then "<" else if x > y then ">" else "="

convert :: String -> Int
convert s =
  case s of
    "A" -> 10
    "B" -> 11
    "C" -> 12
    "D" -> 13
    "E" -> 14
    "F" -> 15
