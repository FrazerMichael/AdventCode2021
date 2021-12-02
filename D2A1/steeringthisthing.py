#Michael Frazer
#Advent of Code 2021
#Day 2, Question 1: Driving this thing
import re

with open('SteeringData.txt', 'r') as file:
    steeringList = file.read().split()

def splitList(list):
    ints = []
    words = []
    for i in list:
        if re.match('^\d+$', i):
            ints.append(int(i))
        else :
            words.append(i)
    return ints, words

deltaList, directionList = splitList(steeringList)

def locationCalculator(a, b):
    depth = 0
    movement = 0

    for i in range(len(a)):
        if a[i] == 'forward':
            movement += b[i]

        elif a[i] == 'up':
            depth -= b[i]

        elif a[i] == 'down':
            depth += b[i]

        else:
            print('bad data')

    return(depth * movement)

print(locationCalculator(directionList, deltaList))
locationCalculator(directionList, deltaList)




