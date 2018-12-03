from gmpy2 import invert

# Needed values
multiple = 3
point = (5, 1)
prime = 17
a = 2

# Special mod function to make sure x mod x = x, not x mod x = 0
def mod(int, p):
    if (int == p):
        return int
    elif ((int < p) and (int >= 0)):
        return int;
    else:
        return (int % p)

# Function that assures s will be a whole number
def sValue(num, den, prime):
    s = prime + 1
    if ((num % den) == 0):
        s = mod((num//den), prime)
    else:
        s = mod((num * invert(den, prime)), prime)

    if (s > prime):
        print "ya messed up"
        exit()

    return s

# Calculate a point addition
def newPoint(pointOne, pointTwo, prime, s):
    x = mod((((s**2) - pointOne[0]) - pointTwo[0]), prime)
    y = mod(((s * (pointOne[0] - x)) - pointOne[1]), prime)
    return (x, y)

# Calculate s value for doubling and double
def double(point, prime, a):
    # Calculate s value
    sn = (3 * (point[0]**2)) + a
    sd = 2 * point[1]
    s = sValue(sn, sd, prime)

    # Calculate and return point
    return newPoint(point, point, prime, s)

# Calculate s value for addition and add
def add(pointOne, pointTwo, prime):
    # Calculate s value
    sn = (pointTwo[1] - pointOne[1])
    sd = (pointTwo[0] - pointOne[0])
    s = sValue(sn, sd, prime)

    # Calculate and return point
    return newPoint(pointOne, pointTwo, prime, s)

# Converts int to binary, removes leading '0b' and the greatest bit
# Returns sequence as a list
def getSequence(multiple):
    return list(bin(multiple)[3:])

currentPoint = point
for x in getSequence(multiple):
    if (int(x) == 1):
        currentPoint = double(point, prime, a)
        currentPoint = add(point, currentPoint, prime)
    else:
        currentPoint = double(currentPoint, prime, a)


print str(multiple) + "P" + " = " + "(" + str(currentPoint[0]) + "," + str(currentPoint[1]) +")"


