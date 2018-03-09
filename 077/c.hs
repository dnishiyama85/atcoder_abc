import Data.List
import Data.Array.IO
import Control.Monad
import Data.Maybe
import qualified Data.ByteString.Char8 as BC8

type Arr = IOUArray Int Int

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- newListArray (0, n - 1) =<< (sort . map (fst . fromJust . BC8.readInt) . BC8.words) <$> BC8.getLine :: IO Arr
  bs <- (sort . map (fst . fromJust . BC8.readInt) . BC8.words) <$> BC8.getLine :: IO [Int]
  cs <- newListArray (0, n - 1) =<< (sort . map (fst . fromJust . BC8.readInt) . BC8.words) <$> BC8.getLine :: IO Arr
  print =<< solve as bs cs n

solve :: Arr -> [Int] -> Arr -> Int -> IO Int
solve as bs cs n = do
  -- bList <- getElems bs
  counts <- forM bs $ \b -> solveB as b cs n
  return $ sum counts

solveB :: Arr -> Int -> Arr -> Int -> IO Int
solveB as b cs n = do
  upperA <- upperBound as b n
  lowerC <- lowerBound cs b n
  -- putStrLn $ printf "b = %d, upperA = %d, lowerC = %d" b upperA lowerC
  return ((upperA + 1) * (n - lowerC))

upperBound :: Arr -> Int -> Int -> IO Int
upperBound arr k n = _upperBound (-1) n
  where
    _upperBound :: Int -> Int -> IO Int
    _upperBound left right
      | right - left <= 1 = return left
      | otherwise = do
          let center = (left + right) `div` 2
          cVal <- readArray arr center
          if cVal < k
            then _upperBound center right
            else _upperBound left center

lowerBound :: Arr -> Int -> Int -> IO Int
lowerBound arr k n = _lowerBound (-1) n
    where
      _lowerBound :: Int -> Int -> IO Int
      _lowerBound left right
        | right - left <= 1 = return right
        | otherwise = do
            let center = (left + right) `div` 2
            cVal <- readArray arr center
            if cVal <= k
              then _lowerBound center right
              else _lowerBound left center
