import random
class Team:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

draftorder = []

draftorder.append( Team('Detroit Red Wings', 1))
draftorder.append( Team('Ottawa Senators', 2))
draftorder.append( Team('Ottawa Senators (from San Jose)', 3))
draftorder.append( Team('Los Angeles Kings', 4))
draftorder.append( Team('Anaheim Ducks', 5))
draftorder.append( Team('New Jersey Devils', 6))
draftorder.append( Team('Buffalo Sabres', 7))
draftorder.append( Team('Montreal Canadiens', 8))
draftorder.append( Team('Chicago Blackhawks', 9))
draftorder.append( Team('New Jersey Devils (from Arizona)', 10))
draftorder.append( Team('Minnesota Wild', 11))
draftorder.append( Team('Winnipeg Jets', 12))
draftorder.append( Team('New York Rangers', 13))
draftorder.append( Team('Florida Panthers', 14))
draftorder.append( Team('Columbus Blue Jackets', 15))

winpos = 0
r = random.randint(0, 999)
for i in range(1000):
    if (i == 185 or i == 320 or i == 435 or i == 530 or i == 615 or i == 690 or
        i == 755 or i == 815 or i == 865 or i == 900 or i == 930 or i == 955 or
        i == 975 or i == 990):
        winpos += 1    
    if (i == r):
        firstplace = draftorder[winpos].name
        break

print(firstplace)
print(r)
print(winpos)

for obj in draftorder:
    print(obj.pos, obj.name, sep = ' ')

    

