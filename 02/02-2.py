


sum = 0

file = open("02-input.txt", "r")
Lines = file.readlines()
file.close()

class color:
  def __init__(self, c, a):
    self.color = c
    self.amount = a

red = color("red", 0)
green = color("green", 0)
blue = color("blue", 0)

colors = [red, green, blue]

def reset_color_amounts():
   for color in colors:
      color.amount = 0

for line in Lines:
    possible = True
    sets = line.split(":")
    game = sets[0].split()[1]
    sets = sets[1].replace(",", " ").split(";")
    for i, set in enumerate(sets):
        divided_set = set.split()
        for j, type in enumerate(divided_set):
            for color in colors:
                if type == color.color:
                    if int(divided_set[j-1]) > color.amount:
                        color.amount = int(divided_set[j-1])
    tempcalc = 0
    for color in colors:
       if tempcalc == 0:
          tempcalc += color.amount
       else:
          tempcalc *= color.amount
    sum += tempcalc
    reset_color_amounts()

print("The sum of all powers in sets is: " + str(sum))

