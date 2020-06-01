import Data.Char

main :: IO ()
main = do
  ws <- words <$> getLine
  putStrLn $ map (toUpper . head) ws
