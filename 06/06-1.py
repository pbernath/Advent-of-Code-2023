
# Input
Time = [60, 80, 86, 76]
Distance = [601, 1163, 1559, 1300]

# Test input
# Time = [7, 15, 30]
# Distance = [9, 40, 200]

answer = 0

for i, ms in enumerate(Time):
    better = 0
    for press_time in range(ms):
        travel_time = ms - press_time
        distance = press_time * travel_time
        if distance > Distance[i]:
            better += 1
    if answer == 0:
        answer += better
    else:
        answer *= better
    print("There are " + str(better) + " ways to beat the record of race " + str(i))

print("The multiplied answer is " + str(answer))






