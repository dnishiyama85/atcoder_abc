import qualified Data.Map as Map
import Control.Monad
import Control.Monad.ST
import Data.STRef

main :: IO ()
main = do
  [n, m] <- (map read . words) <$> getLine :: IO [Int]
  (graph, edges) <- buildGraph (Map.fromList [] ) [] m
  print $ length [True | rm <- edges, bfs graph 1 rm < n]

buildGraph graph edges 0 = return (graph, edges)
buildGraph graph edges n = do
  [a, b] <- (map read . words) <$> getLine :: IO [Int]
  let graph' = Map.insertWith (++) a [b] graph
  let graph'' = Map.insertWith (++) b [a] graph'
  buildGraph graph'' ((a, b):edges) (n - 1)

-- あるノードから辿れるノードの総数を求める
bfs :: Map.Map Int [Int] -> Int -> (Int, Int) -> Int
bfs graph start rm = runST $ do
  visitedRef <- newSTRef (Map.fromList [] :: Map.Map Int Bool)
  count <- newSTRef (0 :: Int)
  let queue = [start]
      loop [] = return ()
      loop queue = do
        let p:queue' = queue
        let maybeNeighbors = Map.lookup p graph
        case maybeNeighbors of
          Nothing -> undefined
          Just neighbors ->
            forM_ neighbors $ \n -> do
              visited <- readSTRef visitedRef
              let v = Map.lookup n visited
              case v of
                Just True -> return ()
                Nothing ->
                  if (p == fst rm && n == snd rm) || (p == snd rm && n == fst rm)
                    then return ()
                    else do
                      let visited' = Map.insert n True visited
                      writeSTRef visitedRef visited'
                      modifySTRef count (+1)
                      loop (queue' ++ [n])

  loop queue
  readSTRef count
