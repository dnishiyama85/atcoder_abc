main :: IO ()
main = do
  ss <- words <$> getLine :: IO [String]
  putStrLn $ "A" ++ take 1 (ss!!1) ++ "C"
