#Michael Frazer
#Advent of Code 2021
#Day 1, Question 1: Sonar Question

with open('SonarData.txt', 'r') as file:
    sonarData = file.read().splitlines()

largerMeasurements = 0

for i in range(0, len(sonarData)):
    if i == 0:
        continue

    if int(sonarData[i]) > int(sonarData[i - 1]):
        largerMeasurements += 1

print(largerMeasurements)