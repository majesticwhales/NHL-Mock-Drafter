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

winpos2 = 0
while (winpos2 == 0 or winpos2 == winpos):
    winpos2 = 0
    r2 = random.randint(0,999)
    for i in range(1000):
        if (i == 165 or i == 295 or i == 408 or i == 504 or i == 591 or
            i == 669 or i == 737 or i == 800 or i == 853 or i == 891 or 
            i == 924 or i == 951 or i == 973 or i == 990):
            winpos2 += 1    
    if (i == r2):
        secondplace = draftorder[winpos2].name
        break


print(firstplace)
print(secondplace)
print(r)
print(r2)
print(winpos)
print(winpos2)

for obj in draftorder:
    print(obj.pos, obj.name, sep = ' ')

    

