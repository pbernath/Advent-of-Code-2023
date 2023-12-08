
file = open("08-input.txt", "r")
Lines = file.readlines()
file.close()

# First test case, expected result 2
# Lines = [
#     "RL",
#     "",
#     "AAA = (BBB, CCC)",
#     "BBB = (DDD, EEE)",
#     "CCC = (ZZZ, GGG)",
#     "DDD = (DDD, DDD)",
#     "EEE = (EEE, EEE)",
#     "GGG = (GGG, GGG)",
#     "ZZZ = (ZZZ, ZZZ)"]

# Second test case, expected result 6
# Lines = [
#     "LLR",
#     "",
#     "AAA = (BBB, BBB)",
#     "BBB = (AAA, ZZZ)",
#     "ZZZ = (ZZZ, ZZZ)"]

class node:
    def __init__(self, n, l, r):
        self.name = n
        self.next_left = l
        self.next_right = r
        # print("Creating node " + self.name + ", with left as " + self.next_left + ", and right as " + self.next_right + "!")

path = Lines[0].rstrip()

nodes = []
for line in Lines:
    if line.find("=") != -1:
        node_name = (line.split("=")[0].rstrip())
        node_next_left = (line.split("=")[1].split(",")[0].lstrip().lstrip("("))
        node_next_right = (line.split("=")[1].split(",")[1].lstrip().rstrip().rstrip(")"))
        nodes.append(node(node_name, node_next_left, node_next_right))

starting_point = None
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
    if node.name == "AAA":
        starting_point = node
    # print("Node name " + node.name + ", with left as " + node.next_left.name + ", and right as " + node.next_right.name + "!")

# print("starting point is:")
# print(starting_point)

current_step = starting_point
steps_taken = 0
while current_step.name != "ZZZ":
    # print("going through all the paths")
    for step in path:
        # print("current step is:")
        # print(current_step)
        if current_step.name == "ZZZ":
            break
        if step == "L":
            current_step = current_step.next_left
        elif step == "R":
            current_step = current_step.next_right
        else:
            print("SOMETHING WRONG WITH THE PATH! " + step)
        steps_taken += 1

print("Steps taken to reach goal: " + str(steps_taken))









