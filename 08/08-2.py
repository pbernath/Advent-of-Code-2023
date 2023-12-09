from math import lcm

file = open("08-input.txt", "r")
Lines = file.readlines()
file.close()

# Test case, expected result 6
# Lines = [
#     "LR",
#     "",
#     "11A = (11B, XXX)",
#     "11B = (XXX, 11Z)",
#     "11Z = (11B, XXX)",
#     "22A = (22B, XXX)",
#     "22B = (22C, 22C)",
#     "22C = (22Z, 22Z)",
#     "22Z = (22B, 22B)",
#     "XXX = (XXX, XXX)"]

class node:
    def __init__(self, n, l, r):
        self.name = n
        self.next_left = l
        self.next_right = r
        self.loop = []
        # print("Creating node " + self.name + ", with left as " + self.next_left + ", and right as " + self.next_right + "!")

path = Lines[0].rstrip()

nodes = []
for line in Lines:
    if line.find("=") != -1:
        node_name = (line.split("=")[0].rstrip())
        node_next_left = (line.split("=")[1].split(",")[0].lstrip().lstrip("("))
        node_next_right = (line.split("=")[1].split(",")[1].lstrip().rstrip().rstrip(")"))
        nodes.append(node(node_name, node_next_left, node_next_right))

starting_points = []
for node in nodes:
    destinations = [node.next_left, node.next_right]
    for i, destination in enumerate(destinations):
        for nextnode in nodes:
            if destination == nextnode.name:
                if i == 0:
                    node.next_left = nextnode
                elif i == 1:
                    node.next_right = nextnode
                break
    if node.name[-1] == "A":
        starting_points.append(node)


loops = []
for i in range(len(starting_points)):
    loops.append([])
found_loops = 0


starts = len(starting_points)
ends = 0

print("Starting on " + str(starts) + " locations")
current_steps = starting_points
steps_taken = 0
while starts != ends and starts != found_loops:
    for step in path:
        # print("Currently on " + str(ends) + " Z-ends")
        if starts == ends:
            break
        else:
            ends = 0
        
        # print("------ Taking a step: " + step)
        for i, concurrent_step in enumerate(current_steps):
            if step == "L":
                # print("Going from " + concurrent_step.name + " to " + concurrent_step.next_left.name)
                current_steps[i] = concurrent_step.next_left
            elif step == "R":
                # print("Going from " + concurrent_step.name + " to " + concurrent_step.next_right.name)
                current_steps[i] = concurrent_step.next_right
            else:
                print("SOMETHING WRONG WITH THE PATH! " + step)
            
            if current_steps[i].name[-1] == "Z":
                ends += 1
                # print("WE ON Z! Paths on Z: " + str(ends))
                loops[i].append(steps_taken + 1)
                for loop in loops:
                    if len(loop) > 5:
                        found_loops += 1
                if found_loops != 6:
                    found_loops = 0

        steps_taken += 1
        if steps_taken % 1_000_000 == 0:
            print(f'{steps_taken:_}')
    if starts == ends:
        print("All starts have reached their ends " + str(ends))

print("Steps taken to reach goal: " + str(steps_taken))

print("--------------------------")

confirmed_loop_lengths = []
for loop in loops:
    print("Found the following loops")
    print(loop)

    if loop[0] * 2 == loop[1] and loop[0] * 3 == loop[2] and loop[0] * 4 == loop[3]:
        confirmed_loop_lengths.append(loop[0])
    else:
        print("CAN NOT CONFIRM LOOP LENGTH FROM START, NEED ANOTHER APPROACH")


print("--------------------------")
print("Confirmed loop lengths:")
print(confirmed_loop_lengths)

print("--------------------------")
print("Lowest Common Multiple (LCM) for the loops is: " + str(lcm(*confirmed_loop_lengths)))



