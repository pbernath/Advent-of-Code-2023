
# file = open("05-input.txt", "r")
# Lines = file.readlines()
# file.close()

file = open("05-test_input.txt", "r")
Lines = file.readlines()
file.close()


# Create list of seeds
seed_input = []
for line in Lines:
    if "seeds" in line:
        seed_input = line.split(":")[1].split()

# seeds = []
# for i, input in enumerate(seed_input):
#     if i % 2 == 0:
#         counter = 0
#         while counter < int(seed_input[i+1]):
#             seeds.append(int(input)+counter)
#             counter += 1

input_variables = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
input_map_names = []
maps = []

# Create all maps
for i, variable in enumerate(input_variables):
    if i < len(input_variables)-1:
        input_map_names.append(input_variables[i] + "-to-" + input_variables[i+1])
        maps.append([])
        section_start = -1
        for j, line in enumerate(Lines):
            if section_start != -1:
                if "\n" == line:
                    break
                else:
                    maps[i].append(line.split())
                    for k, thing in enumerate(maps[-1][-1]):
                        maps[-1][-1][k] = int(thing)
            if input_map_names[i] in line:
                section_start = j

        print(input_map_names[i] + " map:")
        print(maps[i])

print(maps)

# lowest_location = -1

# for i, seed in enumerate(seeds):
#     value = seed
#     print("working on seed " + str(value))
#     for j, map in enumerate(maps):
#         # print("working on map  " + input_map_names[j])
#         # print("value is: " + str(value))
#         for k, rule in enumerate(map):
#             # print("working on rule " + str(rule))
#             # print("checking if value is bigger than or equal to " + str(rule[1]))
#             if value >= rule[1]:
#                 # print("IT IS!")
#                 # print("checking if value is less than or equal to " + str(rule[1]+rule[2]))
#                 if value <= rule[1]+rule[2]:
#                     # print("Updating value from " + str(value) + " to " + str(rule[0]+value-rule[1]))
#                     value = rule[0]+value-rule[1]
#                     break
#     if lowest_location == -1 or value < lowest_location:
#         lowest_location = value

# print("Lowest location is " + str(lowest_location))





