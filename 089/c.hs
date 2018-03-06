import Control.Monad

main :: IO ()
main = do
  n <- readLn :: IO Int
  names <- replicateM n getLine :: IO [String]
  let numM = length $ filter (\name -> head name == 'M') names
      numA = length $ filter (\name -> head name == 'A') names
      numR = length $ filter (\name -> head name == 'R') names
      numC = length $ filter (\name -> head name == 'C') names
      numH = length $ filter (\name -> head name == 'H') names

      c1 = numM * numA * numR
      c2 = numM * numA * numC
      c3 = numM * numA * numH
      c4 = numM * numR * numC
      c5 = numM * numR * numH
      c6 = numM * numC * numH
      c7 = numA * numR * numC
      c8 = numA * numR * numH
      c9 = numA * numC * numH
      c10 = numR * numC * numH

      ans = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10

  print ans
