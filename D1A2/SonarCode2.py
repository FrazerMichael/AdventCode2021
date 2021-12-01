#Michael Frazer
#Advent of Code 2021
#Day 1, Question 2: Sonar Question diving deeper

with open('SonarData.txt', 'r') as file:
    sonarData = file.read().splitlines()

def slidingWindowCalculator(a, b, c):
    totalSum = a + b +c
    return totalSum

largerMeasurements = 0

for i in range(0, len(sonarData)):
    if i == len(sonarData) - 2:
        break

    if i == 0:
        continue

    windowA = slidingWindowCalculator(int(sonarData[i]), int(sonarData[i + 1]), int(sonarData[i + 2]))
    windowB = slidingWindowCalculator(int(sonarData[i - 1]), int(sonarData[i]), int(sonarData[i + 1]))

    if windowA > windowB:
        largerMeasurements += 1

print(largerMeasurements)