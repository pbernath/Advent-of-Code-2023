
file = open("14-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input before expansion, expected outcome 136
# Lines = [
#     "O....#....",
#     "O.OO#....#",
#     ".....##...",
#     "OO.#O....O",
#     ".O.....O#.",
#     "O.#..O.#.#",
#     "..O..#O..O",
#     ".......O..",
#     "#....###..",
#     "#OO..#...."]


dish = []
for i in range(len(Lines[0])):
    dish.append([])

for y, line in enumerate(Lines):
    line = line.strip()
    for x, x_pos in enumerate(line):
        dish[x].append(x_pos)

# print("-------------")

# for column in dish:
#     print(column)

# print("-------------")


for x, column in enumerate(dish):
    for y, row in enumerate(column):
        # print(f"Checking [{x}, {y}]")
        if row == "O" and y != 0:
            current = y
            next = y-1
            for i in range(y-1, -1, -1):
                # print(f"We're on column {x} and row {y}. Current is {current}, next is {next}")
                match column[next]:
                    case ".":
                        column[next] = "O"
                        column[current] = "."
                        current -= 1
                        next -= 1
                    case "#" | "O":
                        break


# for column in dish:
#     print(column)

# print("-------------")

total_load = 0

for x, column in enumerate(dish):
    for y, row in enumerate(column):
        if row == "O":
            total_load += len(column) - y



print(f"The total load on the north support beam is {total_load}")








