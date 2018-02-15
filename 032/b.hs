import Data.List

main :: IO ()
main = do
  s <- getLine :: IO String
  k <- readLn :: IO Int
  if k > length s
    then putStrLn "0"
    else do
      let list = map (\i -> take k $ drop i s) [0..length s - k]
      print $ length $ nub list
