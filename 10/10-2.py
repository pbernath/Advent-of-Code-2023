
file = open("10-input.txt", "r")
Lines = file.readlines()
file.close()



# test sketch, expexted result 4 tiles inside
# Lines = [
#     "...........",
#     ".S-------7.",
#     ".|F-----7|.",
#     ".||.....||.",
#     ".||.....||.",
#     ".|L-7.F-J|.",
#     ".|..|.|..|.",
#     ".L--J.L--J.",
#     "..........."]


# test sketch, expexted result 4 tiles inside
# Lines = [
#     "..........",
#     ".S------7.",
#     ".|F----7|.",
#     ".||....||.",
#     ".||....||.",
#     ".|L-7F-J|.",
#     ".|..||..|.",
#     ".L--JL--J.",
#     ".........."]


# test sketch, expexted result 8 tiles inside
# Lines = [
#     ".F----7F7F7F7F-7....",
#     ".|F--7||||||||FJ....",
#     ".||.FJ||||||||L7....",
#     "FJL7L7LJLJ||LJ.L-7..",
#     "L--J.L7...LJS7F-7L7.",
#     "....F-J..F7FJ|L7L7L7",
#     "....L7.F7||L7|.L7L7|",
#     ".....|FJLJ|FJ|F7|.LJ",
#     "....FJL-7.||.||||...",
#     "....L---J.LJ.LJLJ..."]


# test sketch, expexted result 10 tiles inside
# Lines = [
#     "FF7FSF7F7F7F7F7F---7",
#     "L|LJ||||||||||||F--J",
#     "FL-7LJLJ||||||LJL-77",
#     "F--JF--7||LJLJ7F7FJ-",
#     "L---JF-JLJ.||-FJLJJ7",
#     "|F|F-JF---7F7-L7L|7|",
#     "|FFJF7L7F-JF7|JL---7",
#     "7-L-JL7||F7|L7F-7F7|",
#     "L.L7LFJ|||||FJL7||LJ",
#     "L7JLJL-JLJLJL--JLJ.L"]


sketch = []
path_loop = []
for i in range(len(Lines[0].strip())):
    sketch.append([])
    path_loop.append([])


for y, line in enumerate(Lines):
    # print(f"line {y}")
    line = line.strip()
    for x, x_pos in enumerate(line):
        sketch[x].append(x_pos)
        path_loop[x].append([x, y, "unknown", x_pos])



starting_position = None
for x, column in enumerate(sketch):
    for y, row in enumerate(column):
        if row == "S":
            starting_position = [x, y]
        

# print(starting_position)
# print(sketch)

def find_path (origin, path):
    path_loop[path[0]][path[1]][2] = "path"
    original_direction = [path[0] - origin[0], path[1] - origin[1]]
    tile = sketch[path[0]][path[1]]
    # print(f"We're on {path} with symbol {tile}")
    match original_direction:
        case [-1, 0]:
            original_direction = "left"
        case [1, 0]:
            original_direction = "right"
        case [0, -1]:
            original_direction = "up"
        case [0, 1]:
            original_direction = "down"
        case [0, 0]:
            original_direction = "Starting position"
    # print(f"Move to get here was {original_direction}")
    # checking if loop continues left
    if original_direction != "right" and (tile == "7" or tile == "J" or tile == "-" or tile == "S"):
        destination = [path[0]-1, path[1]]
        # print(f"Checking Left: {destination}")
        if destination[0] >= 0 and destination[0] < len(sketch) and destination[1] >= 0 and destination[1] < len(sketch[0]):
            match sketch[destination[0]][destination[1]]:
                case "F" | "L" | "-":
                    # print("Match!")
                    return path, destination
                case "S":
                    # print("Got back to start! Ending!")
                    return path, destination
    # checking if loop continues right
    if original_direction != "left" and (tile == "F" or tile == "L" or tile == "-" or tile == "S"):
        destination = [path[0]+1, path[1]]
        # print(f"Checking Right: {destination}")
        if destination[0] >= 0 and destination[0] < len(sketch) and destination[1] >= 0 and destination[1] < len(sketch[0]):
            match sketch[destination[0]][destination[1]]:
                case "7" | "J" | "-":
                    # print("Match!")
                    return path, destination
                case "S":
                    # print("Got back to start! Ending!")
                    return path, destination
    # checking if loop continues up
    if original_direction != "down" and (tile == "L" or tile == "J" or tile == "|" or tile == "S"):
        destination = [path[0], path[1]-1]
        # print(f"Checking Up: {destination}")
        if destination[0] >= 0 and destination[0] < len(sketch) and destination[1] >= 0 and destination[1] < len(sketch[0]):
            match sketch[destination[0]][destination[1]]:
                case "F" | "7" | "|":
                    # print("Match!")
                    return path, destination
                case "S":
                    # print("Got back to start! Ending!")
                    return path, destination
    # checking if loop continues down
    if original_direction != "up" and (tile == "F" or tile == "7" or tile == "|" or tile == "S"):
        destination = [path[0], path[1]+1]
        # print(f"Checking Down: {destination}")
        if destination[0] >= 0 and destination[0] < len(sketch) and destination[1] >= 0 and destination[1] < len(sketch[0]):
            match sketch[destination[0]][destination[1]]:
                case "L" | "J" | "|":
                    # print("Match!")
                    return path, destination
                case "S":
                    # print("Got back to start! Ending!")
                    return path, destination
    print("This hopefully will never trigger! AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return 0

# Apparently recursion was too deep for python, so had to switch it up for a while-loop instead...

previous_position, current_position = find_path(starting_position, starting_position)
first_position = current_position
last_position = None
while current_position != starting_position:
    previous_position, current_position = find_path(previous_position, current_position)
    last_position = previous_position


# print(first_position)
# print(last_position)

starting_direction = [first_position[0] - starting_position[0], first_position[1] - starting_position[1]]
match starting_direction:
    case [-1, 0]:
        starting_direction = "left"
    case [1, 0]:
        starting_direction = "right"
    case [0, -1]:
        starting_direction = "up"
    case [0, 1]:
        starting_direction = "down"

ending_direction = [starting_position[0] - last_position[0], starting_position[1] - last_position[1]]
match ending_direction:
    case [-1, 0]:
        ending_direction = "left"
    case [1, 0]:
        ending_direction = "right"
    case [0, -1]:
        ending_direction = "up"
    case [0, 1]:
        ending_direction = "down"

actual_S =""
match starting_direction:
    case "left":
        match ending_direction:
            case "left":
                print("LEFT-LEFT-Start should be a -")
                actual_S = "-"
            case "right":
                print("LEFT-RIGHT-IMPOSSIBLE")
            case "up":
                print("LEFT-UP-Start should be a 7")
                actual_S = "7"
            case "down":
                print("LEFT-DOWN-Start should be a J")
                actual_S = "J"
    case "right":
        match ending_direction:
            case "left":
                print("RIGHT-LEFT-IMPOSSIBLE")
            case "right":
                print("RIGHT-RIGHT-Start should be a -")
                actual_S = "-"
            case "up":
                print("RIGHT-UP-Start should be a F")
                actual_S = "F"
            case "down":
                print("RIGHT-DOWN-Start should be a L")
                actual_S = "L"
    case "up":
        match ending_direction:
            case "left":
                print("UP-LEFT-Start should be a L")
                actual_S = "L"
            case "right":
                print("UP-RIGHT-Start should be a J")
                actual_S = "J"
            case "up":
                print("UP-UP-Start should be a |")
                actual_S = "|"
            case "down":
                print("UP-DOWN-IMPOSSIBLE")
    case "down":
        match ending_direction:
            case "left":
                print("DOWN-LEFT-Start should be a 7")
                actual_S = "7"
            case "right":
                print("DOWN-RIGHT-Start should be a F")
                actual_S = "F"
            case "up":
                print("DOWN-UP-IMPOSSIBLE")
            case "down":
                print("DOWN-DOWN-Start should be a |")
                actual_S = "|"


# print(path_loop[starting_position[0]][starting_position[1]])
path_loop[starting_position[0]][starting_position[1]][3] = actual_S
sketch[starting_position[0]][starting_position[1]] = actual_S
# print(path_loop[starting_position[0]][starting_position[1]])



for y in range(len(sketch[0])):
    for x in range(len(sketch)):
        # print(f"[{x}][{y}] out of [{len(sketch)}][{len(sketch[0])}] at {path_loop[x][y]}")
        if path_loop[x][y][2] == "unknown":
            path_loop[x][y][3] = "."
            sketch[x][y] = "."



tiles_inside = 0
inside = []
for y in range(len(sketch[0])):
    borders = 0
    decider = ""
    for x in range(len(sketch)):
        # print(f"checking {path_loop[x][y]}")
        if path_loop[x][y][2] == "path":
            # print(f"it's path! decider is '{decider}' and sketch is {sketch[x][y]}")
            match decider:
                case "":
                    match sketch[x][y]:
                        case "|":
                            # print(f"|, so decider doesn't change and borders increased from {borders} to {borders+1}")
                            borders += 1
                        case "F" | "L":
                            # print(f"F or L, so nothing replaced with {sketch[x][y]}")
                            decider = sketch[x][y]
                case "F":
                    match sketch[x][y]:
                        case "L":
                            # print("L, so F replaced with L")
                            decider = sketch[x][y]
                        case "|" | "J":
                            # print(f"| or J, so F replaced with nothing and borders increased from {borders} to {borders+1}")
                            decider = ""
                            borders += 1
                        case "7":
                            # print("7, so F replaced with nothing")
                            decider = ""
                case "L":
                    match sketch[x][y]:
                        case "F":
                            # print("F, so L replaced with F")
                            decider = sketch[x][y]
                        case "J":
                            # print("J, so L replaced with nothing")
                            decider = ""
                        case "|" | "7":
                            # print(f"| or 7, so L replaced with nothing and borders increased from {borders} to {borders+1}")
                            decider = ""
                            borders += 1
        if sketch[x][y] == ".":
            match borders % 2:
                case 0:
                    path_loop[x][y][2] = "outside"
                case 1:
                    path_loop[x][y][2] = "inside"
                    tiles_inside += 1
                    inside.append(path_loop[x][y])
                    # print(f"border cound is at {borders}, so half has a remainder of {borders % 2}")
                    # print(f"this is an inner point {path_loop[x][y]} {sketch[x][y]}")


# FF  nothing
# FL  new
# FJ  BORDER
# F7  reset
# LF  new
# LL  nothing
# LJ  reset
# L7  BORDER
#  F  new
#  L  new
#  J  nothing
#  7  nothing












print(f"There are {tiles_inside} tiles inside")

# print(starting_position)
# print(inside)
# for i in range(len(sketch[0])):
#     print(f"{i} {sketch[i][109]}")


