


sum = 0

file = open("02-input.txt", "r")
Lines = file.readlines()
file.close()

class rules:
  def __init__(self, c, a):
    self.color = c
    self.amount = a
 
red = rules("red", 12)
green = rules("green", 13)
blue = rules("blue", 14)

theRules = [red, green, blue]

for line in Lines:
    possible = True
    sets = line.split(":")
    game = sets[0].split()[1]
    sets = sets[1].replace(",", " ").split(";")
    for i, set in enumerate(sets):
        divided_set = set.split()
        for j, type in enumerate(divided_set):
            for rules in theRules:
                if type == rules.color:
                    if rules.amount < int(divided_set[j-1]):
                        # print("setting game " + game + " as not possible")
                        possible = False
        if possible == False:
            break
    if possible == True:
        # print("Game " + game + " is possible")
        sum += int(game)

print("The sum of all valid games is: " + str(sum))

