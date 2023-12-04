# I really should have cleaned this code up better, but just re-used most of the stuff from part 1...

import re

sum = 0

file = open("03-input.txt", "r")
Lines = file.readlines()
file.close()

# test case, expected result 467835
# Lines = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598.."]

#Lines = [".....*......................-..........................*...204........156......7............*................/.717*..................296....", "..826.....924.......................956..............920..................259.-......$......286........6..955.........................=..457", "......124*......................48.....=...435..............12.....886....*........411..........*170..%............90..-295.624............."]

arrayed = list(Lines)

class gear:
  def __init__(self, n, x, y):
    self.number = n
    self.x_pos = x
    self.y_pos = y

gears = []

def checkIndex(x, y, max_x, number):
    for j in range(-1, 2):
        for i in range(-1, 2):
            #print("relpos " + str(i) + "," + str(j))
            if x+i >= 0 and y+j >= 0 and x+i < max_x and y+j < len(Lines):
                #print("checking reltive position " + str(i) + "," + str(j))
                #print("checking actual position " + str(x+i) + "," + str(y+j))
                #print("actual char: " + arrayed[y+j][x+i])
                if arrayed[y+j][x+i].isalnum() == False and arrayed[y+j][x+i] != ".":
                    #print("returning True")
                    if arrayed[y+j][x+i] == "*":
                        if len(gears) > 0:
                            if gears[-1].number != number or gears[-1].x_pos != x+i or gears[-1].y_pos != y+j:
                                gears.append(gear(number, x+i, y+j))
                        else:
                            gears.append(gear(number, x+i, y+j))

                    

for i, line in enumerate(Lines):
    numbers = re.findall(r'[0-9]+', line)
    #print(i)
    #print(numbers)
    index = 0

    for number in numbers:
        #print("working on " + number)
        adjecancy = False
        length = len(number)
        index = line.find(number, index)
        #print("check Left at index " + str(index))
        adjecancy = checkIndex(index, i, len(line)-1, number)
        index += length-1
        if adjecancy != True:
            #print("check Right at index " + str(index))
            adjecancy = checkIndex(index, i, len(line)-1, number)
        if adjecancy == True:
            #print("adding " + number)
            sum += int(number)
        index += 1

# for i, gear in enumerate(gears):
#     print(str(gear.number) + " " + str(gear.x_pos) + ", " + str(gear.y_pos))
# print("---")
for first_gear in gears:
    for second_gear in gears:
        if first_gear.number != second_gear.number and first_gear.x_pos == second_gear.x_pos and first_gear.y_pos == second_gear.y_pos:
            # print(first_gear.number)
            # print(second_gear.number)
            sum += int(first_gear.number) * int(second_gear.number)
            first_gear.number = 0
            second_gear.number = 0


print("The sum of all gear ratios in the schematic is: " + str(sum))
