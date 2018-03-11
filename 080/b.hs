main :: IO ()
main = do
  n <- readLn :: IO Int
  putStrLn $ if isHarshad n then "Yes" else "No"

isHarshad n = n `mod` (digitSum n 0) == 0

digitSum n carry
  | n < 10 = carry + n
  | otherwise = digitSum (n `div` 10) (carry + n `mod` 10)
