main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- (map read . words) <$> getLine :: IO [Int]
  let mul4 = length $ filter (\a -> a `mod` 4 == 0) as
      mul2 = length $ filter (\a -> a `mod` 2 == 0 && a `mod` 4 /= 0) as
  putStrLn $ if (n - 2 * mul4 - 1 <= 0) || (mul4 == 0 && n == mul2) || (n - 2 * mul4 - mul2 <= 0)
              then "Yes"
              else "No"
