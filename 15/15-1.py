
file = open("15-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input before expansion, expected outcome 52
# Lines = ["HASH"]

# Test input before expansion, expected outcome 1320
# Lines = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]


steps = Lines[0].strip().split(",")

# print(steps)

result = 0
multiplier = 17
hash_limit = pow(2, 8) # 256

for sequence in steps:
    current_value = 0
    for char in sequence:
        current_value += ord(char)
        current_value *= multiplier
        current_value %= hash_limit
    result += current_value


print(f"The result is {result}")











