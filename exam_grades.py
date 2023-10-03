import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades =(data.split(','))
grades= list(map(int, grades))
print(grades)

minimum = min(grades)
maximum = max(grades)

print(minimum)
print(maximum)

sumgrades = sum(grades)

averagegrades = sumgrades/len(grades)
averagegradesrounded = round(averagegrades, 2)

print(averagegradesrounded)

averagegradesmean = statistics.mean(grades)

print(averagegradesmean)

averagegradesmedian = statistics.median(grades)

print(averagegradesmedian)

gradesroundup = "Minimum grade:{minimum}, Maximum grade:{maximum}, Average grade:{averagegrades}, Mean grade:{averagegradesmean}, Median grade:{averagegradesmedian}"

print(gradesroundup.format(minimum = 14, maximum = 100, averagegrades = 53.18, averagegradesmean = 53.17741935483871, averagegradesmedian = 50.0))