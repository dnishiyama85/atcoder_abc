import Data.List

main :: IO ()
main = do
  taro <- readLn :: IO Int
  jiro <- readLn :: IO Int
  saburo <- readLn :: IO Int
  let d = sortBy (flip compare) [(taro, "taro"), (jiro, "jiro"), (saburo, "saburo")]
  let ranking = [ snd _d | _d <- d　] :: [String]
  let [Just r1, Just r2, Just r3] = elemIndex <$> ["taro", "jiro", "saburo"] <*> [ranking]
  print $ r1 + 1
  print $ r2 + 1
  print $ r3 + 1
