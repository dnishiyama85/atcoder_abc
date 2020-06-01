import Control.Monad.Trans.State

type Work = Int
type Day = Int
type WorkState = (Work, Day)

work :: State WorkState Work
work = do
  (workLeft, daysLeft) <- get
  let todaysWork = workLeft `div` daysLeft^2
  if daysLeft == 1
    then return workLeft
    else do
      put (workLeft - todaysWork, daysLeft - 1)
      work

main = do
  ws <- getLine
  ds <- getLine
  let w = read ws :: Int
  let d = read ds :: Int
  print $ fst $ runState work (w, d)
