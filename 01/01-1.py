import re

sum = 0

file = open("01-input.txt", "r")
Lines = file.readlines()
file.close()

# example calibration values, expected result is 142
# Lines = {"1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"}

for line in Lines:
    digits = re.findall(r'\d', line)
    sum += int(digits[0] + digits[-1])

print("The sum of all calibration values is: " + str(sum))