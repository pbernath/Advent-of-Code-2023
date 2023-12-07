from collections import Counter

file = open("07-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected answer is 6440
# Lines = [
#     "32T3K 765",
#     "T55J5 684",
#     "KK677 28",
#     "KTJJT 220",
#     "QQQJA 483"]


sets = []
for line in Lines:
    sets.append(line.split())
    sets[-1][-1] = int(sets[-1][-1])

# print(sets)


def checkType (hand):
    workingHand = Counter(hand).most_common()

    match workingHand[0][1]:
        
        # five of a kind, type 7
        case 5: return 7

        # four of a kind, type 6
        case 4: return 6

        # three of the same
        case 3:
            if workingHand[1][1] == 2:
                # full house, type 5
                return 5
            else:
                # three of a kind, type 4
                return 4
        
        # two of the same
        case 2:
            if workingHand[1][1] == 2:
                # two pair, type 3
                return 3
            else:
                # one pair, type 2
                return 2
        
        # all other cases
        case _: return 1


def numberfyCards (hand):
    numberfied = []
    for char in hand:
        match char:
            case "2":
                numberfied.append(2)
            case "3":
                numberfied.append(3)
            case "4":
                numberfied.append(4)
            case "5":
                numberfied.append(5)
            case "6":
                numberfied.append(6)
            case "7":
                numberfied.append(7)
            case "8":
                numberfied.append(8)
            case "9":
                numberfied.append(9)
            case "T":
                numberfied.append(10)
            case "J":
                numberfied.append(11)
            case "Q":
                numberfied.append(12)
            case "K":
                numberfied.append(13)
            case "A":
                numberfied.append(14)
            case _:
                print("SOMETHING IS BROKEN WITH NUMBERFYING CARDS!")
    
    return numberfied





sortedSets = [[], [], [], [], [], [], []]
for set in sets:
    set.append(numberfyCards(set[0]))
    set.append(checkType(set[2]))
    sortedSets[set[3] -1].append(set)

for type in sortedSets:
    type.sort(key=lambda x: (x[2][0], x[2][1], x[2][2], x[2][3], x[2][4]))


# print(sortedSets)


answer = 0
rank = 1
for type in sortedSets:
    for hand in type:
        answer += hand[1] * rank
        rank += 1


print("Total winnings: " + str(answer))






