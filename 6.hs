task1B :: [Int]
task1B = [x | x <- [1..100], x `mod` 4 /= 0]

task2A :: Int -> Bool
task2A n = not (null [ 1 | a <- [100..999],
                           n `mod` a == 0,
                           b <- [100..999],
                           (n `div` a) `mod` b == 0,
                           let c = n `div` (a * b),  
                           c >= 100 && c <= 999 ])

task3A :: String -> Bool
task3A str = case words str of
    [] -> True
    (firstWord:otherWords) ->
        let firstLetter = head firstWord
        in all (\w -> head w == firstLetter) otherWords

task4B :: (Real f, Fractional f) => [[f]] -> f
task4B xss =
    let maxes = map maximum xss
    in sum maxes / fromIntegral (length maxes)

task5A :: Int -> [Int]
task5A n = [x | x <- [1..n], n `mod` x == 0]