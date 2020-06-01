import Control.Monad

main :: IO ()
main = do
  strs <- replicateM 12 getLine :: IO [String]
  print $ length $ filter ('r' `elem`) strs
