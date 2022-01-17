import csv
import math
from turtle import st

with open("data.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# function to find mean
def Mean(data):
    n = len(data)
    total = 0

    for component in data:
        total += int(component)
    
    mean = total/n
    return mean

squared_value = []

for i in data:
    a = int(i) - Mean(data)
    a = a**2
    squared_value.append(a)

sum = 0

for i in squared_value:
    sum += i

result = sum/(len(data)-1)

standard_deviation = math.sqrt(result)
print(f"The standard deviation of the given data is: {standard_deviation}")

