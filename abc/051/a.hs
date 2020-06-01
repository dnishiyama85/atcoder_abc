main :: IO ()
main = unwords . split <$> getLine >>= putStrLn

split = _split []
_split ts "" = ts
_split ts s = _split (ts ++ [(token s)]) (drop (length(token s) + 1) s)
token = _token ""
_token ys "" = ys
_token ys (x:xs) = do
if x == ','
then ys
else _token (ys ++ [x]) xs
