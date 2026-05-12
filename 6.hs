task1B :: [Int]
task1B = [x | x <- [1..100], x `mod` 4 /= 0]

task2A :: Int -> Bool
task2A n = n `elem` [a * b * c | a <- [100..999], b <- [100..999], c <- [100..999], a * b * c <= n]

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