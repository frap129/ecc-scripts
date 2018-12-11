from pointUtils import add
from pointUtils import double
from pointUtils import getSequence
from pointUtils import printMultiple
from pointUtils import EXAM_MODE

def printAdd(currentPoint, pDiff):
    print str(pDiff)+"P + 1P = (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")"

# Needed values
multiple = 13
point = (5, 9)
prime = 11
a = 1


# For showing work
currentMultiple = 1

currentPoint = point
for x in getSequence(multiple):
    if (int(x) == 1):
        currentPoint = double(point, prime, a)
        if (EXAM_MODE):
            currentMultiple = currentMultiple * 2
            printMultiple(currentPoint, currentMultiple)
        currentPoint = add(point, currentPoint, prime)
        if (EXAM_MODE):
            printAdd(currentPoint, currentMultiple)
            currentMultiple = currentMultiple + 1
    else:
        currentPoint = double(currentPoint, prime, a)
        if (EXAM_MODE):
            printMultiple(currentPoint, currentMultiple*2)

printMultiple(currentPoint, multiple)
