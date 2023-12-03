import re

sum = 0

file = open("03-input.txt", "r")
Lines = file.readlines()
file.close()

# test case, expected result 4361
# Lines = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+..58",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598.."]

#Lines = [".....*......................-..........................*...204........156......7............*................/.717*..................296....", "..826.....924.......................956..............920..................259.-......$......286........6..955.........................=..457", "......124*......................48.....=...435..............12.....886....*........411..........*170..%............90..-295.624............."]

arrayed = list(Lines)

def checkIndex(x, y, max_x):
    for j in range(-1, 2):
        for i in range(-1, 2):
            #print("relpos " + str(i) + "," + str(j))
            if x+i >= 0 and y+j >= 0 and x+i < max_x and y+j < len(Lines):
                #print("checking reltive position " + str(i) + "," + str(j))
                #print("checking actual position " + str(x+i) + "," + str(y+j))
                #print("actual char: " + arrayed[y+j][x+i])
                if arrayed[y+j][x+i].isalnum() == False and arrayed[y+j][x+i] != ".":
                    #print("returning True")
                    return True

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
        adjecancy = checkIndex(index, i, len(line)-1)
        index += length-1
        if adjecancy != True:
            #print("check Right at index " + str(index))
            adjecancy = checkIndex(index, i, len(line)-1)
        if adjecancy == True:
            #print("adding " + number)
            sum += int(number)
        index += 1

print("The sum of all parts in schematic is: " + str(sum))
