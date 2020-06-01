import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  [sa, sb, sc] <- replicateM 3 getLine
  putStrLn [play (sa, sb, sc) 'a']

play :: (String, String, String) -> Char -> Char
play (sa, sb, sc) now
  | now == 'a' && null sa = 'A'
  | now == 'b' && null sb = 'B'
  | now == 'c' && null sc = 'C'
  | otherwise =
      case now of
        'a' -> let (p:sa') = sa in play (sa', sb, sc) p
        'b' -> let (p:sb') = sb in play (sa, sb', sc) p
        'c' -> let (p:sc') = sc in play (sa, sb, sc') p
