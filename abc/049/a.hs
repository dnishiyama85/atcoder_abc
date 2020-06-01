main :: IO ()
main = do
  c <- head <$> getLine :: IO Char
  putStrLn $ if elem c "aeiou" then "vowel" else "consonant"
