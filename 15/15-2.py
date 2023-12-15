
file = open("15-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input before expansion, expected outcome 145
# Lines = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]


steps = Lines[0].strip().split(",")

# print(steps)

focusing_power = 0
multiplier = 17
hash_limit = pow(2, 8) # 256
hashmap = []
for i in range(hash_limit):
    hashmap.append([])


for sequence in steps:
    current_value = 0
    for char in sequence:
        if char == "=" or char == "-":
            break
        current_value += ord(char)
        current_value *= multiplier
        current_value %= hash_limit
    current_label = ""
    found = False
    if sequence.find("=") != -1:
        current_label = sequence.split("=")[0]
        for label in hashmap[current_value]:
            if label[0] == current_label:
                label[1] = int(sequence[-1])
                found = True
                break
        if found == False:
            hashmap[current_value].append([sequence.split("=")[0], int(sequence[-1])])
    else:
        current_label = sequence.split("-")[0]
        for i, label in enumerate(hashmap[current_value]):
            if label[0] == current_label:
                # print(f"Popping {hashmap[current_value][i]}")
                hashmap[current_value].pop(i)
    
    # print(f'After "{sequence}" going for box {current_value}:')
    # for i, box in enumerate(hashmap):
    #     if i == 4:
    #         break
    #     print(f"Box {i}: {box}")
    # print("")

# print(f'Final results:')
for i, box in enumerate(hashmap):
    for j, label in enumerate(box):
        focusing_power +=  (i + 1) * (j + 1) * label[1]
    # print(f"Box {i}: {box}")
print(f"The focusing power is {focusing_power}")











