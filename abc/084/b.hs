import Text.Regex.Posix
import Text.Printf

main :: IO ()
main = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  s <- getLine
  let regex = printf "[0-9]{%d}-[0-9]{%d}" a b :: String
  putStrLn $ if s =~ regex then "Yes" else "No"
