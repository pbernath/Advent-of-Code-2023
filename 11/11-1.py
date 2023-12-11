
file = open("11-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input before expansion, expected outcome 374
# Lines = [
#     "...#......",
#     ".......#..",
#     "#.........",
#     "..........",
#     "......#...",
#     ".#........",
#     ".........#",
#     "..........",
#     ".......#..",
#     "#...#....."]


universe = []
for i in range(len(Lines[0])):
    universe.append([])

empty_rows = []
for y, line in enumerate(Lines):
    # print(f"line {y}")
    line = line.strip()
    empty_spaces = 0
    for x, x_pos in enumerate(line):
        # print(f"position {x} is {x_pos} from {line}")
        if x_pos == ".":
            empty_spaces += 1
        universe[x].append(x_pos)
    if empty_spaces == len(line):
        empty_rows.append(y)

empty_columns = []
for x, column in enumerate(universe):
    if set(column) == {"."}:
        empty_columns.append(x)
    already_inserted = 0
    for row in empty_rows:
        column.insert(row+already_inserted, ".")
        already_inserted += 1


already_inserted = 0
for column in empty_columns:
    universe.insert(column+already_inserted, universe[column+already_inserted])
    already_inserted += 1

# print(f"Empty rows = {len(empty_rows)}")
# print(empty_rows)
# print(f"Empty columns = {len(empty_columns)}")
# print(empty_columns)



# test_image = []
# for i in range(len(universe[0])):
#     test_image.append("")

# for x in universe:
#     for i, y in enumerate(x):
#         test_image[i] = str(test_image[i]) + str(y)

# for line in test_image:
#     print(line)

# # Test input after expansion, expected outcome 374
# Lines = [
#     "....#........",
#     ".........#...",
#     "#............",
#     ".............",
#     ".............",
#     "........#....",
#     ".#...........",
#     "............#",
#     ".............",
#     ".............",
#     ".........#...",
#     "#....#......."]

# for i, line in enumerate(Lines):
#     if line == test_image[i]:
#         print(f"Line {i} is correct")
#     else:
#         print(f"Line {i} is WRONG!!!")


galaxies = []
for x, row in enumerate(universe):
    for y, column in enumerate(row):
        if column == "#":
            for galaxy in galaxies:
                galaxy[1].append([x, y])
            galaxies.append([[x, y], []])


path_length_sum = 0
for galaxy in galaxies:
    for path in galaxy[1]:
        path_length_sum += abs(galaxy[0][0] - path[0]) + abs(galaxy[0][1] - path[1])

print(f"The sum of all path lengths is {path_length_sum}")

