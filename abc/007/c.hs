import Control.Monad
import Debug.Trace

main :: IO ()
main = do
  [r, _c]  <- (map read . words) <$> getLine :: IO [Int]
  [sy, sx] <- (map read . words) <$> getLine :: IO [Int]
  [gy, gx] <- (map read . words) <$> getLine :: IO [Int]
  maze <- replicateM r $ convert <$> getLine :: IO [[Int]]
  let maze' = setval maze (sx - 1, sy - 1) 0
      solvedMaze = wfs maze' [(sx - 1, sy - 1)]
  print $ solvedMaze !! (gy - 1) !! (gx - 1)

wall :: Int
wall = -2

unexplored :: Int
unexplored = -1 :: Int

convert :: [Char] -> [Int]
convert = map (\c -> if c == '#' then wall else unexplored)

type Point = (Int, Int)
type Queue = [Point]
type Maze = [[Int]]

wfs :: Maze -> Queue -> Maze
wfs maze []    = maze
wfs maze queue =
  let (x, y):queue' = queue
      points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] :: [Point]
      distance = maze !! y !! x
      (maze'', queue'') = searchAll distance points maze queue'
  in
    wfs maze'' queue''

searchAll :: Int -> [Point] -> Maze -> Queue -> (Maze, Queue)
searchAll _ [] maze queue = (maze, queue)
searchAll distance points maze queue =
  let p:points' = points
      (maze', queue') = search distance p maze queue
  in
    searchAll distance points' maze' queue'

search :: Int -> Point -> Maze -> Queue -> (Maze, Queue)
search distance point maze queue
  | val == wall       = (maze, queue)
  | val == unexplored =
    let maze' = setval maze point (distance + 1)
    in (maze', queue ++ [point])
  | otherwise = (maze, queue)
  where
    (x, y) = point
    val = maze !! y !! x

setval :: Maze -> Point -> Int -> Maze
setval maze (x, y) val =
  let
    row'  = replace x val (maze !! y)
  in replace y row' maze

replace pos newVal list = take pos list ++ newVal : drop (pos+1) list

debugprint :: Maze -> String
debugprint = unlines . map (\row -> unwords [show v | v <- row])
