from itertools import pairwise

file = open("09-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected outcome 114
# Lines = [
#     "0 3 6 9 12 15",
#     "1 3 6 10 15 21",
#     "10 13 16 21 30 45"]


history = []
for line in Lines:
    history.append(line.strip().split(" "))
    for i, value in enumerate(history[-1]):
        history[-1][i] = int(history[-1][i])


def extrapolator(sequence):
    # print("Starting on sequence")
    # print(sequence)
    if set(sequence) == {0}:
        # print("This sequence is all 0, return 0")
        return 0
    
    new_sequence = [b - a for a, b in pairwise(sequence)]

    # print("New sequence is")
    # print(new_sequence)
    # print("Calling the function again with the new sequence")
    recursive_call = extrapolator(new_sequence)
    # print("Recursive call has returned with the value " + str(recursive_call))
    # print("Adding last of the sequence and return from recursive call together to return to caller")
    # print(str(sequence[-1]) + " + " + str(recursive_call) + " = " + str(sequence[-1] + recursive_call))
    return sequence[-1] + recursive_call


combined_prediction = 0
for readings in history:
    # print("Starting with new readings")
    # print(readings)
    prediction = extrapolator(readings)
    # print("Extrapolator has returned with the prediction of " + str(prediction))
    combined_prediction += prediction


print("The sum of extrapolated values is: " + str(combined_prediction))

