{-# LANGUAGE LambdaCase #-}

import Data.IORef
import Control.Monad

main :: IO ()
main = do
  s <- getLine
  st <- newIORef ""
  forM_ s $ \case
      '0' -> modifyIORef st (++ ['0'])
      '1' -> modifyIORef st (++ ['1'])
      'B' -> do
        now <- readIORef st
        unless (null now) $ modifyIORef st init
  putStrLn =<< readIORef st
