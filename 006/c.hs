import Text.Printf

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  let candidates = [ (-2 * b + m - 2 * n, b)| b <- [0..m `div` 2 - n]]
      answers = filter (\(e, b) -> e <= -b + n) candidates
  putStrLn $ if null answers
              then "-1 -1 -1"
              else do
                 let (e, b) = head answers
                     a = n - b - e
                 printf "%d %d %d" a e b
