
file = open("10-input.txt", "r")
Lines = file.readlines()
file.close()

# test sketch with complex loop, expexted result 8
# Lines = [
#     "..F7.",
#     ".FJ|.",
#     "SJ.L7",
#     "|F--J",
#     "LJ..."]

# test sketch with complex loop and extra non-main-loop tiles, expexted result 8
# Lines = [
#     "7-F7-",
#     ".FJ|7",
#     "SJLL7",
#     "|F--J",
#     "LJ.LJ"]



sketch = []
for i in range(len(Lines[0])):
    sketch.append([])

for y, line in enumerate(Lines):
    # print(f"line {y}")
    line = line.strip()
    for x, x_pos in enumerate(line):
        sketch[x].append(x_pos)


starting_position = None
for x, column in enumerate(sketch):
    for y, row in enumerate(column):
        if row == "S":
            starting_position = [x, y]
            break
    if starting_position != None:
        break

# print(starting_position)

total_steps_taken = 0

def find_path (origin, path):
    original_direction = [path[0] - origin[0], path[1] - origin[1]]
    tile = sketch[path[0]][path[1]]
    # print(f"We're on {path} with symbol {tile}")
    match original_direction:
        case [-1, 0]: original_direction = "left"
        case [1, 0]: original_direction = "right"
        case [0, -1]: original_direction = "up"
        case [0, 1]: original_direction = "down"
        case [0, 0]: original_direction = "Starting position"
    # print(f"Move to get here was {original_direction}")
    # checking if loop continues left
    if original_direction != "right" and (tile == "7" or tile == "J" or tile == "-" or tile == "S"):
        destination = [path[0]-1, path[1]]
        # print(f"Checking Left: {destination}")
        if destination[0] > 0 or destination[0] < len(sketch)-1 or destination[1] > 0 or destination[1] < len(sketch[0])-1:
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
        if destination[0] > 0 or destination[0] < len(sketch)-1 or destination[1] > 0 or destination[1] < len(sketch[0])-1:
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
        if destination[0] > 0 or destination[0] < len(sketch)-1 or destination[1] > 0 or destination[1] < len(sketch[0])-1:
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
        if destination[0] > 0 or destination[0] < len(sketch)-1 or destination[1] > 0 or destination[1] < len(sketch[0])-1:
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
total_steps_taken += 1
while current_position != starting_position:
    previous_position, current_position = find_path(previous_position, current_position)
    total_steps_taken += 1



print(f"Moved a total of {total_steps_taken} steps")
print(f"The point furthest from the starting location is {int(total_steps_taken/2)} steps away")



