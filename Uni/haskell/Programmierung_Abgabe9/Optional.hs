-- optional Implementation

data Optional a = Empty | Present a deriving Show

mapOptional :: (a -> b) -> Optional a -> Optional b
mapOptional f Empty = Empty
mapOptional mapFunction (Present a) = Present (mapFunction a)

filterOptional :: (a -> Bool) -> Optional a -> Optional a
filterOptional filterFunction Empty         = Empty
filterOptional filterFunction (Present a)   | not (filterFunction a) = Empty
                                            | otherwise = Present a

foldOptional :: (a -> b) -> b -> Optional a -> b
foldOptional foldFunction standardValue Empty       = standardValue
foldOptional foldFunction standardValue (Present a) = foldFunction a

-- product implementation

data Product = Article String Int deriving Show

isHumanEatable :: Product -> Bool
isHumanEatable (Article name price) | name == "Dog Food" = False 
                                    | otherwise  = True

adjustPrice :: Product -> Product
adjustPrice (Article name price) = Article name newPrice
                                where newPrice  | price < 1000 = price*2
                                                | otherwise = price
            
stringify :: Product -> String
stringify (Article name price) = "The article " ++ name ++ " costs " ++ show price ++ " Cent."

toPriceTag :: Product -> String
toPriceTag article = stringifyO (adjustPriceO (filterHumanEatable article))

filterHumanEatable :: Product -> Optional Product
filterHumanEatable product = filterOptional isHumanEatable (Present product)  

adjustPriceO :: Optional Product -> Optional Product
adjustPriceO article = mapOptional adjustPrice article

stringifyO :: Optional Product -> String
stringifyO article = foldOptional stringifyO "This article is currently unavailable." article