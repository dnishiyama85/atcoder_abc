import Data.List

main :: IO ()
main = do
  w <- getLine
  let counts = (map length . group . sort) w
  putStrLn $ if all even counts then "Yes" else "No"
