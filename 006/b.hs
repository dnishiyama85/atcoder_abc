main :: IO ()
main = do
  end <- readLn :: IO Int
  let trib = tribonacci 1 1 0 0 end
  print trib

tribonacci :: Int -> Int -> Int -> Int -> Int -> Int
tribonacci n a2 a1 a0 end
  | end == 1 = 0
  | end == 2 = 0
  | end == 3 = 1
  | n == (end - 2) = a2
  | otherwise =
      let a3 = (a2 + a1 + a0) `mod` 10007 in tribonacci (n + 1) a3 a2 a1 end
