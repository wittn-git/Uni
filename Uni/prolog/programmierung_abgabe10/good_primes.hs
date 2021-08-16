-- primes

from :: Int -> [Int]
from n = n : from (n+1)

dropMult :: Int -> [Int] -> [Int]
dropMult x = filter (\y -> mod y x /= 0)

dropAll :: [Int] -> [Int]
dropAll (h:xs) = h : dropAll (dropMult h xs)

primes :: [Int]
primes = dropAll (from 2)

-- helper functions

multiplyLists :: [Int] -> [Int] -> [Int]
multiplyLists (h1:xs) (h2:ys)   = (h1*h2) : multiplyLists xs ys

zipPrimes :: [Int] -> [Int] -> [Int]
zipPrimes (a:xs) (b:ys) | b == 0 || a*a < b = zipPrimes xs ys
                        | otherwise         = a : zipPrimes xs ys

-- good primes

goodPrimes :: [Int]
goodPrimes = zipPrimes primes (multiplyLists (0:primes) (drop 1 primes))             