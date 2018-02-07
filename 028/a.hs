main :: IO ()
main = do
  n <- readLn :: IO Int
  putStrLn $ solve n

solve n
  | n <= 59 = "Bad"
  | n <= 89 = "Good"
  | n <= 99 = "Great"
  | n <= 100 = "Perfect"
