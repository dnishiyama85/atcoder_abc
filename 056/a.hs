main :: IO ()
main = do
  [a, b] <- words <$> getLine :: IO [String]
  putStrLn $ case (a, b) of
               ("H", "H") -> "H"
               ("H", "D") -> "D"
               ("D", "H") -> "D"
               ("D", "D") -> "H"
