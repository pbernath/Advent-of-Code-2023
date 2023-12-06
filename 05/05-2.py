
file = open("05-input.txt", "r")
Lines = file.readlines()
file.close()

# file = open("05-test_input.txt", "r")
# Lines = file.readlines()
# file.close()


# Create list of seeds
seed_input = []
for line in Lines:
    if "seeds" in line:
        seed_input = line.split(":")[1].split()

seeds = []
for i, input in enumerate(seed_input):
    if i % 2 == 0:
        seeds.append([int(seed_input[i]), int(seed_input[i+1])])

# print(seeds)


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

        # print(input_map_names[i] + " map:")
        # print(maps[i])

for map in maps:
    map.sort(key=lambda x: x[1])

# print(maps)

lowest_location = -1

for seed in seeds:
    value_range = []
    value_range.append(seed)
    # print("checking seed:")
    # print(seed)

    for k, map in enumerate(maps):
        split_values = []
        # print("checking map " + input_map_names[k] + ":")
        # print(map)
        for i, range in enumerate(value_range):
            # print("checking range:")
            # print(range)
            for j, rule in enumerate(map):
                # print("checking rule:")
                # print(rule)
                # print("checking range[0] (" + str(range[0]) + ") >= rule[1] (" + str(rule[1]) + ")")
                if range[0] >= rule[1]:
                    # print("it is!")
                    # print("checking range[0] + range[1] (" + str(range[0] + range[1]) + ") <= rule[1] + rule[2] (" + str(rule[1] + rule[2]) + ")")
                    # print("checking range[0] + range[1] - rule[1] - rule[2] (" + str(range[0] + range[1] - rule[1] - rule[2]) + ") <= range[1] (" + str(range[1]) + ")")
                    if range[0] + range[1] <= rule[1] + rule[2]:
                        # print("first of above checks passed")
                        split_values.append(range)
                        # print("appending the following:")
                        # print(split_values[-1])
                        break
                    elif range[0] + range[1] - rule[1] - rule[2] <= range[1]:
                        # print("second of above checks passed")
                        split_values.append([range[0], rule[1] + rule[2] - range[0]])
                        value_range[i] = [rule[1] + rule[2], range[0] + range[1] - rule[1] - rule[2]]
                        range = value_range[i]
                        # print("appending the following:")
                        # print(split_values[-1])
                        # print("keeping this to iterate over:")
                        # print(range)
                elif range[0] + range[1] >= rule[1]:
                    # print("it isn't, BUT, needs to be split!")
                    split_values.append([range[0], rule[1] - range[0]])
                    value_range[i] = [rule[1], range[1] - rule[1] + range[0]]
                    range = value_range[i]
                    # print("appending the following:")
                    # print(split_values[-1])
                    # print("keeping this to iterate over:")
                    # print(range)
                # else:
                #     print("it isn't")
                if j == len(map) -1:
                    split_values.append(range)
                    # print("no map a match, keeping values")
                    # print("appending the following:")
                    # print(split_values[-1])
                    break
        # print("SPLITTING COMPLETE, TRANLATING MAP")
        # print("printing the split_values")
        # print(split_values)
        new_values = []
        for range in split_values:
            # print("workting on range:")
            # print(range)
            for j, rule in enumerate(map):
                # print("working on rule")
                # print(rule)
                if range[0] + range[1] -1 >= rule[1] and range[0] + range[1] <= rule[1] + rule[2]:
                    new_values.append([rule[0] + range[0] - rule[1], range[1]])
                    # print("appending modified value and breaking")
                    break
                if j == len(map) -1:
                    # print("appending unmodified value")
                    new_values.append(range)
        # print("printing the new values")
        # print(new_values)
        value_range = new_values
    for range in value_range:
        if lowest_location == -1 or range[0] < lowest_location:
            lowest_location = range[0]

print("Lowest location is " + str(lowest_location))





