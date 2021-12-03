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
    aim = 0
    depth = 0
    movement = 0

    for i in range(len(a)):
        if a[i] == 'forward':
            x = b[i]
            movement += x
            depth += aim * x

        elif a[i] == 'up':
            aim -= b[i]

        elif a[i] == 'down':
            aim += b[i]

        else:
            print('bad data')

    return(depth * movement)

print(locationCalculator(directionList, deltaList))
locationCalculator(directionList, deltaList)