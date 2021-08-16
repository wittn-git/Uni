-- data type declaration

data MultTree a = DataNode a | IndexNode a a [MultTree a] deriving Show 

--helper functions

extremeOf :: (Int -> Int -> Int) -> [Int] -> Int 
extremeOf _ []              = 0 
extremeOf function (h:xs)   = extremeHelper function h xs 

extremeHelper :: (Int -> Int -> Int) -> Int -> [Int] -> Int
extremeHelper _ x []      = x
extremeHelper function x (h:xs)  
                            | xs == [] = k
                            | otherwise = extremeHelper function k xs
                            where k = function x h

mapTo :: [a] -> (a -> b) -> [b]
mapTo [] _              = []
mapTo (h:xs) function   = function h : mapTo xs function

forEach :: [MultTree a] -> (MultTree a -> [b]) -> [b]
forEach [] _                               = []
forEach (DataNode v1 : xs) function        = function (DataNode v1) ++ forEach xs function 
forEach (IndexNode v1 v2 m : xs) function  = function (IndexNode v1 v2 m) ++ forEach xs function

identity :: MultTree a -> MultTree a
identity i = i

asList :: (a -> b) -> a -> [b]
asList function x = [function x]

listContains :: Eq a => [a] -> a -> Bool
listContains [] _ = False
listContains (h:xs) x   | x == h = True
                        | otherwise = True 

--depth
-- Aufgabe leider sehr ungenau gestellt - ist maximale Tiefe (verzweigungsGrad1) oder maximale Anzahl an Kindern eines Knotens gemeint (verzweigungsGrad1)?

verzweigungsGrad1 :: MultTree a -> Int 
verzweigungsGrad1 (DataNode v1)          = 1
verzweigungsGrad1 (IndexNode v1 v2 m)    = 1 + extremeOf max (mapTo m verzweigungsGrad1)

verzweigungsGrad2 :: MultTree a -> Int 
verzweigungsGrad2 (DataNode v1)          = 0
verzweigungsGrad2 (IndexNode v1 v2 m)    = extremeOf max ((length m) : (forEach m (asList verzweigungsGrad2)))

--data list

datenListe :: MultTree a -> [a]
datenListe (DataNode v1)        = [v1]
datenListe (IndexNode v1 v2 m)  = [v1,v2] ++ forEach m datenListe

--data interval

datenIntervalle :: MultTree Int -> MultTree Int
datenIntervalle (DataNode v1) = DataNode v1 
datenIntervalle (IndexNode v1 v2 m) = IndexNode newValue1 newValue2 newChildren  
                                    where   newValue1   | v1 == max v1 v2 = n1 
                                                        | otherwise = n2
                                            newValue2   | v2 == min v1 v2 = n2 
                                                        |otherwise = n1
                                            n1          | hasDataNode (IndexNode v1 v2 m) = extremeOfTree (extremeOf max) (IndexNode v1 v2 m) 
                                                        | otherwise = maxBound 
                                            n2          | hasDataNode (IndexNode v1 v2 m) = extremeOfTree (extremeOf min) (IndexNode v1 v2 m) 
                                                        | otherwise = minBound 
                                            newChildren = forEach m (asList datenIntervalle)

hasDataNode :: MultTree a -> Bool 
hasDataNode (DataNode _) = True 
hasDataNode (IndexNode _ _ m) = listContains (forEach m (asList hasDataNode)) True 

extremeOfTree :: ([Int] -> Int) -> MultTree Int -> Int 
extremeOfTree _ (DataNode v1)               = v1
extremeOfTree function (IndexNode _ _ m)    = function (forEach m (asList (extremeOfTree function)))   

--contains function

contains :: Int -> MultTree Int -> Bool 
contains x (DataNode v1)        = v1 == x
contains x (IndexNode v1 v2 m)  | x == v1 || x == v2 = True
                                | min v1 v2 > x || max v1 v2 < x = False
                                | otherwise = listContains list True 
                                where list = forEach m (asList (contains x))

--tree declaration as const

t1 :: MultTree Int 
t1 = IndexNode 3 42 [IndexNode 3 15 [DataNode 3, DataNode 11, DataNode 12], IndexNode 19 42 [DataNode 42, DataNode 23]]

t2 :: MultTree Int 
t2 = IndexNode 1 1 []