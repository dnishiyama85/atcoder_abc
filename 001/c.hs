main = do
    [deg, dis] <- (map read . words) <$> getLine :: IO [Int]
    let w = calc_wind $ round1(fromIntegral(dis)/ 60)
    let dir = if w == 0 then "C" else calc_dir $ fromIntegral(deg) / 10
    putStrLn $ dir ++ " " ++ (show w)

round1 :: Float -> Float
round1 n = fromIntegral(roundUpOn5(n * 10.0)) / 10.0

roundUpOn5 :: (RealFrac a, Integral b) => a -> b
roundUpOn5 x
  | n <= -0.5 = m - 1
  | n >= 0.5 = m + 1
  | otherwise = m
  where (m, n) = properFraction x

calc_dir :: Float -> String
calc_dir deg
    |  11.25 <= deg && deg <  33.75 = "NNE"
    |  33.75 <= deg && deg <  56.25 = "NE"
    |  56.25 <= deg && deg <  78.75 = "ENE"
    |  78.75 <= deg && deg < 101.25 = "E"
    | 101.25 <= deg && deg < 123.75 = "ESE"
    | 123.75 <= deg && deg < 146.25 = "SE"
    | 146.25 <= deg && deg < 168.75 = "SSE"
    | 168.75 <= deg && deg < 191.25 = "S"
    | 191.25 <= deg && deg < 213.75 = "SSW"
    | 213.75 <= deg && deg < 236.25 = "SW"
    | 236.25 <= deg && deg < 258.75 = "WSW"
    | 258.75 <= deg && deg < 281.25 = "W"
    | 281.25 <= deg && deg < 303.75 = "WNW"
    | 303.75 <= deg && deg < 326.25 = "NW"
    | 326.25 <= deg && deg < 348.75 = "NNW"
    | otherwise                     = "N"

calc_wind :: Float -> Int
calc_wind d
    |  0.0 <= d && d <=  0.2 =  0
    |  0.3 <= d && d <=  1.5 =  1
    |  1.6 <= d && d <=  3.3 =  2
    |  3.4 <= d && d <=  5.4 =  3
    |  5.5 <= d && d <=  7.9 =  4
    |  8.0 <= d && d <= 10.7 =  5
    | 10.8 <= d && d <= 13.8 =  6
    | 13.9 <= d && d <= 17.1 =  7
    | 17.2 <= d && d <= 20.7 =  8
    | 20.8 <= d && d <= 24.4 =  9
    | 24.5 <= d && d <= 28.4 = 10
    | 28.5 <= d && d <= 32.6 = 11
    | 32.7 <= d              = 12

