
#You are playing chinese chopsticks with a friend but to make it more interesting, you decided to comine it with Submarine.

#During your turn, you cannot see the chopsticks and your friend can only give you the coordinates of every chopstick (the initial and final points), and you must tell the number of chopsticks that you can move without affecting any other.

#Inputs

#    The first line contains the value of N, the number of chopsticks
#    The next N lines contain 2 pairs of values. The x and y coordinates of the starting and ending point of a chopstick

#Output

#   The number of chopsticks that can be moved without affecting any other (assume that if there's an intersection between two chopstics, moving one will affect the other)

class Chopstick:
  def __init__(self, start, end):
    self.start = start
    self.end = end

chopsticksArr = []
n = sys.stdin.readline()

for line in sys.stdin:
    if(line is " "):
        continue
    startX = int(line[line.find("(")+1:line.find(",")])
    startY = int(line[line.find(",")+1:line.find(")")])
    endline = line[line.find(")")+2:len(line)]
    endX = int(endline[endline.find("(")+1:endline.find(",")])
    endY = int(endline[endline.find(",")+1:endline.find(")")])
    newChop = Chopstick([startX, startY], [endX, endY])
    chopsticksArr.append(newChop)


def checkIfIntersects(chop1,chop2):
    if(chop1.start[1] >= chop2.start[1] and chop1.end[1] <= chop2.end[1] and chop1.start[0] <= chop2.start[0] and chop1.end[0] >= chop2.end[0]):
        return True
    if(chop1.start[1] <= chop2.start[1] and chop1.end[1] >= chop2.end[1] and chop1.start[0] >= chop2.start[0] and chop1.end[0] <= chop2.end[0]):
        return True
    return False

numChop = 0
for chop1 in chopsticksArr:
    interBool = False
    for chop2 in chopsticksArr:
        if(chop1 is not chop2):
            interBool = checkIfIntersects(chop1,chop2)
        if (interBool):
            break
    if (not interBool):
        numChop = numChop + 1; 

print(numChop)