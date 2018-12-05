from pointUtils import add
from pointUtils import double
from pointUtils import getSequence
from pointUtils import printMultiple

# Needed values
multiple = 15
point = (8, 10)
prime = 29
a = 4

currentPoint = point
for x in getSequence(multiple):
    if (int(x) == 1):
        currentPoint = double(point, prime, a)
        currentPoint = add(point, currentPoint, prime)
    else:
        currentPoint = double(currentPoint, prime, a)


printMultiple(currentPoint, multiple)
