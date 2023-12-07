from collections import Counter

file = open("07-input.txt", "r")
Lines = file.readlines()
file.close()


# Test input, expected answer is 5905
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
    jokers = 0
    for card in workingHand:
        if card[0] == 1:
            jokers = card[1]
    # print(hand)
    # print(workingHand)
    # print("jokers: " + str(jokers))

    if jokers > 0:
        if workingHand[0][0] == 1:
            # print("MOST OF THE JOKERS, MOVE THEM LAST!")
            workingHand.append(workingHand.pop(0))
        elif workingHand[1][0] == 1:
            # print("SECOND MOST OF THE JOKERS, MOVE THEM LAST!")
            workingHand.append(workingHand.pop(1))
        
    # print("new workingHand:")
    # print(workingHand)


    match workingHand[0][1]:
        
        # five of a kind, type 7
        case 5: return 7

        # four of the same
        case 4:
            if jokers == 1:
                # five of a kind with the help of one joker, type 7
                return 7
            else:
                # four of a kind, type 6
                return 6

        # three of the same
        case 3:
            if jokers == 2:
                # five of a kind with the help of two jokers, type 7
                return 7
            elif jokers == 1:
                # four of a kind with the help of one joker, type 6
                return 6
            else:
                if workingHand[1][1] == 2:
                    # full house, type 5
                    return 5
                else:
                    # three of a kind, type 4
                    return 4
        
        # two of the same
        case 2:
            if jokers == 3:
                # five of a kind with the help of three jokers, type 7
                return 7
            elif jokers == 2:
                # four of a kind with the help of one joker, type 6
                return 6
            elif jokers == 1:
                if workingHand[1][1] == 2:
                    # full house with the help of one joker, type 5
                    return 5
                else:
                    # three of a kind with the help of one joker, type 4
                    return 4
            else:
                if workingHand[1][1] == 2:
                    # two pair, type 3
                    return 3
                else:
                    # one pair, type 2
                    return 2
        
        # all other cases
        case _:
            if jokers >= 4:
                # five of a kind with either all jokers or a high card and four jokers, type 7
                return 7
            elif jokers == 3:
                # four of a kind with the help of three jokers, type 6
                return 6
            elif jokers == 2:
                # three of a kind with the help of two jokers, type 4
                return 4
            elif jokers == 1:
                # pair with the help of one joker, type 2
                return 2
            else:
                # high card
                return 1
            



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
                numberfied.append(1)
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






