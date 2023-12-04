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
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


for line in Lines:
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
                if points > 0:
                    #print("Double up!")
                    points *= 2
                if points == 0:
                    #print("You get a point!")
                    points += 1
    
    #print("Total points for this card is " + str(points) + "!")
    sum += points



print("The scratchcards are worth " + str(sum) + " points")
