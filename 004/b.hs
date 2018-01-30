import qualified Control.Monad as M
import Data.Sequence

main = do
    m <- M.replicateM 4 getLine
    let reversed = Prelude.reverse m
    let result = [ Prelude.reverse r | r <- reversed]
    mapM putStrLn result

