
file = open("13-input.txt", "r")
Lines = file.readlines()
file.close()


for i, line in enumerate(Lines):
    Lines[i] = line.strip()


# Test input, expected result 400
# Lines = [
#     "#.##..##.",
#     "..#.##.#.",
#     "##......#",
#     "##......#",
#     "..#.##.#.",
#     "..##..##.",
#     "#.#.##.#.",
#     "",
#     "#...##..#",
#     "#....#..#",
#     "..##..###",
#     "#####.##.",
#     "#####.##.",
#     "..##..###",
#     "#....#..#"]


# for line in Lines:
#     print(f"'{line}'")

patterns = []
i = -1
for k, line in enumerate(Lines):
    if line == "" or k == 0:
        i += 1
        patterns.append([[], []])
        for j in range(len(Lines[k+1])):
            patterns[i][1].append("")
    if line != "":
        patterns[i][0].append(line)
        for j, char in enumerate(line):
            patterns[i][1][j] += char


# print(patterns)




def old_checkmatch(pattern):
    # print("Checking a pattern:")
    # print(pattern)
    for i in range(len(pattern) - 1):
        last_match = [None, None]
        left = i
        right = i+1
        while left >= 0 and right < len(pattern):
            # print(f"Checking if {pattern[left]} == {pattern[right]}")
            if pattern[left] == pattern[right]:
                # print("IT DOES!")
                last_match = [left, right]
                left -= 1
                right += 1
            else:
                break
        # print(f"Checking if last match was edges")
        if last_match[0] == 0 or last_match[1] == len(pattern) - 1:
            # print("They were! So we found a complete match!")
            return i+1
        # print("not edges...")
    return 0




def checkmatch(pattern, skip):
    # print("Checking a pattern:")
    # print(pattern)
    for i in range(len(pattern) - 1):
        if skip == None or i != skip - 1:
            last_match = [None, None]
            left = i
            right = i+1
            misses = 0
            while left >= 0 and right < len(pattern) and misses <= 1:
                for j in range(len(pattern[i])):
                    if pattern[left][j] != pattern[right][j]:
                        misses += 1
                
                # print(f"Checking if misses is <= 1")
                if misses <= 1:
                    # print(f"misses still ok: {misses}")
                    last_match = [left, right]
                    left -= 1
                    right += 1
                else:
                    # print(f"too many misses: {misses}")
                    break
            # print(f"Checking if last match was edges")
            if last_match[0] == 0 or last_match[1] == len(pattern) - 1:
                # print("They were! So we found a complete match!")
                return i+1
            # print("not edges...")
    return 0


for k, pattern in enumerate(patterns):
    patterns[k].append(None)
    patterns[k].append(None)

# for pattern in patterns:
#     print(f"[{pattern[2]}],[{pattern[3]}]")




total_value = 0
for k, pattern in enumerate(patterns):
    print(f"Checking pattern {k}:")
    # print(pattern)
    # for line in pattern[0]:
    #     print(line)
    hit = False

    for i in range(len(pattern)-2):
        value = 0
        multiplier = 0
        rc = ""
        index = 0
        pattern[i+2] = old_checkmatch(pattern[i])
        index = checkmatch(pattern[i], pattern[i+2])
        if i == 0:
            rc = "rows"
            multiplier = 100
        if i == 1:
            rc = "columns"
            multiplier = 1
        value = multiplier * index
        if index != 0:
            print(f"Found match with {rc} at posistions {index-1} and {index} that gives a value of {value}")
            total_value += value
            hit = True
            pattern[i+2] = index
            break
    if hit == False:
        for line in pattern[0]:
            print(line)
        print("no match?")
    print()



print(f"Total value is {total_value}")

# for pattern in patterns:
#     print(f"[{pattern[2]}],[{pattern[3]}]")

















