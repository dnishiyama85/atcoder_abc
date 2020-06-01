import Data.List

main :: IO ()
main = do
  s <- getLine
  let Just h = elemIndex 'A' s
      Just t = elemIndex 'Z' $ reverse s
  print $ (length s - t - 1) - h + 1
