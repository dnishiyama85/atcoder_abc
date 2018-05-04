import qualified Data.Map as Map
import Data.Sequence as Seq
import Control.Monad
import Control.Monad.ST
import Data.STRef

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  graph <- buildGraph (Map.fromList [] ) m
  let (found, dist) = bfs graph n
  putStrLn $ if found && dist <= 2 then "POSSIBLE" else "IMPOSSIBLE"

buildGraph graph 0 = return graph
buildGraph graph n = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  let graph' = Map.insertWith (++) a [b] graph
  let graph'' = Map.insertWith (++) b [a] graph'
  buildGraph graph'' (n - 1)

bfs :: Map.Map Int [Int] -> Int -> (Bool, Int)
bfs graph n = runST $ do
    visitedRef <- newSTRef (Map.fromList [] :: Map.Map Int Bool)
    found <- newSTRef (False, -1)
    let queue = Seq.fromList [(1, 0)]
    let loop queue =
          case Seq.viewl queue of
            Seq.EmptyL -> return ()
            (a, dist) :< queue' ->
              if dist >= 2
                then return ()
                else do
                  let maybeNeighbors = Map.lookup a graph
                  case maybeNeighbors of
                    Nothing -> undefined
                    Just neighbors ->
                      forM_ neighbors $ \m ->
                        if n == m
                          then do
                            -- ゴールについた
                            writeSTRef found (True, dist + 1)
                            return ()
                          else do
                            visited <- readSTRef visitedRef
                            let v = Map.lookup m visited
                            case v of
                              -- すでに訪れた場所
                              Just True -> return ()
                              -- 新しく訪れた場所
                              Nothing -> do
                                let visited' = Map.insert m True visited
                                writeSTRef visitedRef visited'
                                loop (queue' |> (m, dist + 1))

    loop queue
    readSTRef found
