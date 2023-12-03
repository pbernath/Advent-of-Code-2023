import re

sum = 0

file = open("c:/users/nbern/documents/git/aoc/01/01-input.txt", "r")
Lines = file.readlines()
file.close()

# example calibration values, expected result is 281
# Lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

# testing outliers, expexted result is 492
# Lines = ["twone", "eightwo", "nineight", "aaa9a8a", "eighthree", "eeeight", "onetwone", "oooneeone"]

numerical_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
written_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]



for line in Lines:
    lowest_index = -1
    lowest_digit = -1
    highest_index = -1
    highest_digit = -1

    for digit in numerical_digits:

        found_index = line.find(digit)
        if found_index != -1:
            if lowest_index == -1 or found_index < lowest_index:
                lowest_index = found_index
                lowest_digit = digit

        found_index = line.rfind(digit)
        if found_index != -1:
            if highest_index == -1 or found_index > highest_index:
                highest_index = found_index
                highest_digit = digit

    for i, digit in enumerate(written_digits):
        
        found_index = line.find(digit)
        if found_index != -1:
            if lowest_index == -1 or found_index < lowest_index:
                lowest_index = found_index
                lowest_digit = numerical_digits[i]

        found_index = line.rfind(digit)
        if found_index != -1:
            if highest_index == -1 or found_index > highest_index:
                highest_index = found_index
                highest_digit = numerical_digits[i]

    # print(line + " -> " + str(lowest_digit) + str(highest_digit))
    sum += int(str(lowest_digit) + str(highest_digit))

print("The sum of all calibration values is: " + str(sum))