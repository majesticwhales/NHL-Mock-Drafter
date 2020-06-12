import random
class Team:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

class TeamNeed:
    def __init__(self, c, lw, rw, lhd, rhd, g):
        self.c = c
        self.lw = lw
        self.rw = rw
        self.lhd = lhd
        self.rhd = rhd
        self.g = g

standings = []

standings.append( Team('Detroit Red Wings', 1))
standings.append( Team('Ottawa Senators', 2))
standings.append( Team('Ottawa Senators (from San Jose)', 3))
standings.append( Team('Los Angeles Kings', 4))
standings.append( Team('Anaheim Ducks', 5))
standings.append( Team('New Jersey Devils', 6))
standings.append( Team('Buffalo Sabres', 7))
standings.append( Team('Montreal Canadiens', 8))
standings.append( Team('Chicago Blackhawks', 9))
standings.append( Team('New Jersey Devils (from Arizona)', 10))
standings.append( Team('Minnesota Wild', 11))
standings.append( Team('Winnipeg Jets', 12))
standings.append( Team('New York Rangers', 13))
standings.append( Team('Florida Panthers', 14))
standings.append( Team('Columbus Blue Jackets', 15))

winpos = 0
r = random.randint(0, 999)
for i in range(1000):
    if (i == 185 or i == 320 or i == 435 or i == 530 or i == 615 or i == 690 or
        i == 755 or i == 815 or i == 865 or i == 900 or i == 930 or i == 955 or
        i == 975 or i == 990):
        winpos += 1    
    if (i == r):
        firstplace = standings[winpos].name
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
            secondplace = standings[winpos2].name
            break

winpos3 = 0
while (winpos3 == 0 or winpos3 == winpos or winpos3 == winpos2):
    winpos3 = 0
    r3 = random.randint(0,999)
    for i in range(1000):
        if (i == 144 or i == 267 or i == 378 or i == 475 or i == 564 or
            i == 644 or i == 715 or i == 782 or i == 839 or i == 880 or 
            i == 916 or i == 946 or i == 970 or i == 988):
            winpos3 += 1    
        if (i == r3):
            thirdplace = standings[winpos3].name
            break

    
draftorder = []

draftorder.append(Team(standings[winpos].name, 1))
draftorder.append(Team(standings[winpos2].name, 2))
draftorder.append(Team(standings[winpos3].name, 3))

sel = 4

for obj in standings:
    if (obj.name != draftorder[0].name and
        obj.name != draftorder[1].name and
        obj.name != draftorder[2].name):
        draftorder.append(Team(obj.name, sel))
        sel += 1

if (draftorder[0].name == 'New Jersey Devils (from Arizona)'):
    draftorder[0].name = 'Arizona Coyotes'
if (draftorder[1].name == 'New Jersey Devils (from Arizona)'):
    draftorder[1].name = 'Arizona Coyotes'
if (draftorder[2].name == 'New Jersey Devils (from Arizona)'):
    draftorder[2].name = 'Arizona Coyotes'

draftorder.append(Team('Calgary Flames', 16))
draftorder.append(Team('New Jersey Devils (from Vancouver)', 17))
draftorder.append(Team('Nashville Predators', 18))
draftorder.append(Team('Carolina Hurricanes (from Toronto)', 19))
draftorder.append(Team('Edmonton Oilers', 20))
draftorder.append(Team('Ottawa Seantors (from New York Islanders)', 21))
draftorder.append(Team('Dallas Stars', 22))
draftorder.append(Team('New York Rangers (from Carolina)', 23))
draftorder.append(Team('Minnesota Wild (from Pittsburgh)', 24))
draftorder.append(Team('Philadelphia Flyers', 25))
draftorder.append(Team('San Jose Sharks (from Tampa Bay)', 26))
draftorder.append(Team('Colorado Avalanche', 27))
draftorder.append(Team('Vegas Golden Knights', 28))
draftorder.append(Team('Washington Capitals', 29))
draftorder.append(Team('St. Louis Blues', 30))
draftorder.append(Team('Anaheim Ducks (from Boston)', 31))

ranking = []


print("DRAFT ORDER:")
for obj in draftorder:
    print(obj.pos, obj.name, sep = ' ')

    

