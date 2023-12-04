import re

sum = 0

file = open("04-input.txt", "r")
Lines = file.readlines()
file.close()

# test case, expected result 13 points
# Lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 6: 74 18 13 56 72 | 74 77 10 23 35 67 36 11"]

cards = [0] * len(Lines)
#print(cards)

for i, line in enumerate(Lines):
    cards[i] += 1
    points = 0
    rest = line.split(":")
    card = rest[0].split()[1]
    winners = rest[1].split("|")[0].split()
    numbers = rest[1].split("|")[1].split()
    #print("Card " + card)
    #print(winners)
    #print(numbers)

    for winner in winners:
        for number in numbers:
            if winner == number:
                #print(winner + " is a winner!")
                points += 1
    
    #print("Winning numbers on card " + card + " with index " + str(i) + " is " + str(points))
    #print("There are " + str(cards[i]) + " copies of this card")

    for j in range(cards[i]):
        for k in range(points):
            if i+k+1 < len(cards):
                #print("adding a copy of card at index " + str(i+k+1))
                cards[i+k+1] += 1
            #else:
                #print("winner out of bounds, no copy created")
        #print("counting a copy of THIS card at index " + str(i))
        sum += 1




print("Ended up with  " + str(sum) + " scratchcards")
