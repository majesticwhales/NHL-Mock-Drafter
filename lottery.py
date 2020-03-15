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



for obj in draftorder:
    print(obj.pos, obj.name, sep = ' ')

print("Test")
    

