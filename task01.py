#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

file1 = 'task01a.txt'
file2 = "task01b.txt"
file3 = "task01c.txt"


file = open(file1)
data = json.load(file)
largest = max(data)
print(" _________________________________________")
print(f"| The largest number for file 1 is: {largest} |")

fileB = open(file2)
data = json.load(fileB)
largest2 = max(data)
print(f"| The largest number for file 2 is: {largest2} |")

fileC = open(file3)
data = json.load(fileC)
largest3 = max(data)
print(f"| The largest number for file 3 is: {largest3} |")
print(" _________________________________________")






