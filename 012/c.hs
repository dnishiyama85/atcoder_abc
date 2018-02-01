import Text.Printf

total :: Int -- 抜けのないときの総和
total = sum [a*b | a <- [1..9], b <- [1..9]]

main :: IO ()
main = do
  n <- readLn :: IO Int
  let diff = total - n
  putStrLn $ unlines [printf "%d x %d" a b| a <- [1..9], b <- [1..9], a * b == diff]
