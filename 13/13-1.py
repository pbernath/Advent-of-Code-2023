
file = open("13-input.txt", "r")
Lines = file.readlines()
file.close()


for i, line in enumerate(Lines):
    Lines[i] = line.strip()


# Test input, expected result 405
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


def checkmatch(pattern):
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




total_value = 0
for k, pattern in enumerate(patterns):
    print(f"Checking pattern {k}:")
    # for line in pattern[0]:
    #     print(line)
    hit = False

    for i in range(len(pattern)):
        value = 0
        multiplier = 0
        rc = ""
        index = 0
        index = checkmatch(pattern[i])
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
            break
    if hit == False:
        for line in pattern[0]:
            print(line)
        print("no match?")
    print()

print(f"Total value is {total_value}")



















