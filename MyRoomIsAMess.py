#My room is a mess

#A university student has a collection of T-shirts of his favorite soccer teams and he wants to order them according to two characteristics: the team name and the nationality of the team.

#Your task is to help him in his work.

#Inputs:

#    N, the number of T-shirts
#    The following 2N lines contain the team name and the nationality of every T-shirt

#Outputs:

#    An ordered list of T-shirts (ascendingly). First order them by the nationality and if they have the same value, order them by the team name.



class Nation:
  def __init__(self, name, teams):
    self.name = name
    self.teams = teams
    
def lookNation(searchn, nationsArr): 
    for otherNation in nationsArr:
        if(searchn == otherNation.name):
            return otherNation
    return -1


bigArray = []
for line in sys.stdin:
    if line.endswith('\n'):
        line = line[:-1]
    bigArray.append(line)

nations = []
n = bigArray[0]
i=0
for element in bigArray:
    if((i%2)==0 and i!=0):
        if(len(nations)==0 or lookNation(element, nations) == -1):
            teams = [bigArray[i-1]]
            newNat = Nation(element, teams)
            nations.append(newNat)
        else:
            lookNation(element, nations).teams.append(bigArray[i-1])
    i = i+1
    
nations.sort(key=lambda x: x.name)
for nation in nations:
    nation.teams.sort()

for nation in nations:
    for team in nation.teams:
        print(team)