type Expression = (Int, Char, Int)

parse :: String -> Expression
parse s =
  let [a, op, b] = words s
  in (read a, head op, read b)

main :: IO ()
main = do
  (a, op, b) <- parse <$> getLine :: IO Expression
  print $ if op == '+' then a + b else a - b
