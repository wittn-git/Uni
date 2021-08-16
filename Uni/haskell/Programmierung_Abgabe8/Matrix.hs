{-# LANGUAGE ScopedTypeVariables #-} 

isMatrix::[[Int]] -> Bool
isMatrix [] = True 
isMatrix (h:xs) | xs == [] = True
                | length h /= length (xs !! 0) = False 
                | otherwise = isMatrix xs

extract::(Int,Int) -> Int -> Int
extract (x,y) n | n == 0 = x
                | otherwise  = y

dimensions::[[Int]] -> (Int,Int)
dimensions [] = (0,0)
dimensions (h:xs)   | not(isMatrix (h:xs)) = (-1,-1)
                    | otherwise = (1+length xs, length h)

isQuadratic::[[Int]] -> Bool
isQuadratic matrix  | not(isMatrix matrix) = False
                    | extract (dimensions matrix) 0 == extract (dimensions matrix) 1 = True 
                    | otherwise = False 

getRow::[[Int]] -> Int -> [Int] 
getRow matrix row   | not(isMatrix matrix) = []
                    | otherwise = matrix !! row

getColumn::[[Int]] -> Int -> [Int] 
getColumn [] column = []
getColumn (h:xs) column | not(isMatrix (h:xs)) = []
                        | otherwise = h!!column : getColumn xs column

trav::[[Int]] -> [[Int]]
trav matrix = addRowsByColumns matrix 0

addRowsByColumns::[[Int]] -> Int -> [[Int]]
addRowsByColumns matrix col     | col < extract (dimensions matrix) 1 = getColumn matrix col : addRowsByColumns matrix (col+1)
                                | otherwise = []

setVal :: [a] -> Int -> a -> [a]
setVal [] _ _ = []
setVal (x:xs) index val | index == 0 = val:xs
                        | otherwise = x:(setVal xs (index-1) val)

setEntry :: [[Int]] -> Int -> Int -> Int -> [[Int]]
setEntry [] _ _ _       = []
setEntry matrix i j aij | not (isMatrix matrix) = []
                        | otherwise = setVal matrix i (setVal (getRow matrix i) j aij)

--This function adds two matrices, by the usual process. If two matrices with different dimensions are put in as parameters, an emtpy matrix is returned.
addMatrices::[[Int]] -> [[Int]] -> [[Int]]
addMatrices [][] = []
addMatrices (h1:xs) (h2:ys) | dimensions (h1:xs) /= dimensions (h2:ys) = []
                            | otherwise = addRows h1 h2 : addMatrices xs ys

addRows::[Int] -> [Int] -> [Int]
addRows [][] = []
addRows (h1:xs) (h2:ys) = (h1+h2) : addRows xs ys