
file = open("14-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input before expansion, expected outcome 64
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
for i in range(len(Lines[0].strip())):
    dish.append([])

for y, line in enumerate(Lines):
    newline = line.strip()
    # print(f"'{newline}' {y} {len(newline)}")
    for x, x_pos in enumerate(newline):
        dish[x].append(x_pos)


loops = 300

for k in range(loops):
    # print("- starting position -")

    # for y in range(len(dish[0])):
    #     line = ""
    #     for x in range(len(dish)):
    #         line += dish[x][y]
    #     print(line)

    # print("- going north -")

    for x in range(len(dish)):
        for y in range(len(dish[0])):
            # print(f"Checking [{x}, {y}]")
            if dish[x][y] == "O" and y != 0:
                current = y
                next = y-1
                for i in range(y-1, -1, -1):
                    match dish[x][next]:
                        case ".":
                            dish[x][next] = "O"
                            dish[x][current] = "."
                            current -= 1
                            next -= 1
                        case "#" | "O":
                            break

    # for y in range(len(dish[0])):
    #     line = ""
    #     for x in range(len(dish)):
    #         line += dish[x][y]
    #     print(line)

    # print("- going west -")

    for y in range(len(dish[0])):
        for x in range(len(dish)):
            if dish[x][y] == "O" and x != 0:
                current = x
                next = x-1
                for i in range(x-1, -1, -1):
                    match dish[next][y]:
                        case ".":
                            dish[next][y] = "O"
                            dish[current][y] = "."
                            current -= 1
                            next -= 1
                        case "#" | "O":
                            break

    # for y in range(len(dish[0])):
    #     line = ""
    #     for x in range(len(dish)):
    #         line += dish[x][y]
    #     print(line)

    # print("- going south -")

    for x in range(len(dish)):
        for y in range(len(dish[0]) - 1, -1, -1):
            if dish[x][y] == "O" and y != len(dish[0]) - 1:
                current = y
                next = y+1
                for i in range(len(dish[0]) - y - 1):
                    match dish[x][next]:
                        case ".":
                            dish[x][next] = "O"
                            dish[x][current] = "."
                            current += 1
                            next += 1
                        case "#" | "O":
                            break

    # for y in range(len(dish[0])):
    #     line = ""
    #     for x in range(len(dish)):
    #         line += dish[x][y]
    #     print(line)

    # print("- going east -")

    for y in range(len(dish[0])):
        for x in range(len(dish) -1, -1, -1):
            if dish[x][y] == "O" and x != len(dish) -1:
                current = x
                next = x+1
                for i in range(len(dish) - x - 1):
                    match dish[next][y]:
                        case ".":
                            dish[next][y] = "O"
                            dish[current][y] = "."
                            current += 1
                            next += 1
                        case "#" | "O":
                            break

    # for y in range(len(dish[0])):
    #     line = ""
    #     for x in range(len(dish)):
    #         line += dish[x][y]
    #     print(line)

    total_load = 0

    for x, column in enumerate(dish):
        for y, row in enumerate(column):
            if row == "O":
                total_load += len(column) - y

    print(f"The total load on the north support beam after iteration {k+1} is {total_load}")


# Did a real dirty solution, just checked the recurring loop length and what it'd be after 1_000_000_000 iterations and submitted that. I want to revisit this one and do a proper solution without repeating code for the directions as well as the program figuring out the loop length.





