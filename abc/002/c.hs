main = do
    [xa, ya, xb, yb, xc, yc] <- (map read . words) <$> getLine
    let a = xb - xa
        b = yb - ya
        c = xc - xa
        d = yc - ya
        area = abs (a * d - b * c) / 2.0
    putStrLn $ show area

