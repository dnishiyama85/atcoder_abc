import Control.Applicative
import Control.Monad

main = do
    inputs <- map (map read . words) <$> replicateM 3 getLine
    let scores = map (\[a, b] -> a * b `div` 10) inputs
    putStrLn $ show $ sum scores

