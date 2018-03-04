main :: IO ()
main = do
  odd <- getLine
  even <- getLine
  putStrLn $ solve odd even []

solve [] [] carry = carry
solve [o] [] carry = carry ++ [o]
solve odd even carry =
  let o:dd = odd
      e:ven = even
  in solve dd ven (carry ++ [o, e])
