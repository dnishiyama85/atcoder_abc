type Compress = ([(Char, Int)], String)

main :: IO ()
main = do
  s <- getLine
  let result = fst $ process ([(head s, 0)], s) :: [(Char, Int)]
  putStrLn $ foldl (\acc (c, cnt) -> acc ++ [c] ++ show cnt) "" $ reverse result

process :: Compress -> Compress
process (result, []) = (result, [])
process (result, rest) =
  let (lastChar, lastCount):result' = result
      c:rest' = rest
      result'' =
         if c == lastChar
           then (lastChar, lastCount + 1) : result'
           else (c, 1) : result

  in process (result'', rest')
