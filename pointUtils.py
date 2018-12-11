from gmpy2 import invert

EXAM_MODE = False # Set to true to show work

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
    # We know s can't be greater than the prime, therefore
    # prime + 1 will be our sentinel value
    s = prime + 1

    if (den == 0):
        return s # Use sentinel value to denote an infinite point
    elif ((num % den) == 0): # Check if the numerator is evenly divisible
        s = mod((num//den), prime)
    else:
        s = mod((num * invert(den, prime)), prime)

    # s should never be greater than the prime by now
    if (s > prime):
        print "ya messed up"
        exit()

    return s

# Calculate a point addition
def newPoint(pointOne, pointTwo, prime, s):
    x = mod((((s**2) - pointOne[0]) - pointTwo[0]), prime)
    if (EXAM_MODE):
        print "x = "+str(s)+"^2 - "+str(pointOne[0])+" - "+str(pointOne[1])+" mod "+str(prime)
        print "x = "+str(x)
    y = mod(((s * (pointOne[0] - x)) - pointOne[1]), prime)
    if (EXAM_MODE):
        print "y = "+str(s)+"("+str(pointOne[0])+" - "+str(x)+") - "+str(pointOne[1])+" mod "+str(prime)
        print "y = "+str(y)
    return (x, y)

# Calculate s value for doubling and double
def double(point, prime, a):
    # Calculate s value
    sn = (3 * (point[0]**2)) + a
    sd = 2 * point[1]
    s = sValue(sn, sd, prime)
    if (EXAM_MODE):
        print "S = (3 * "+str(point[0])+"^2 + "+str(a)+")/(2 * "+str(point[1])+") mod "+str(prime)
        print "S = "+str(sn)+"/"+str(sd)+" mod "+str(prime)
        print "S = "+str(s)

    # If s > prime, must be an infinite point
    if (s > prime):
        return (0, 0)

    # Calculate and return point
    return newPoint(point, point, prime, s)

# Calculate s value for addition and add
def add(pointOne, pointTwo, prime):
    # Calculate s value
    sn = (pointTwo[1] - pointOne[1])
    sd = (pointTwo[0] - pointOne[0])
    s = sValue(sn, sd, prime)
    if (EXAM_MODE):
        print "S = ("+str(pointTwo[1])+" - "+str(pointOne[1])+")/("+str(pointTwo[0])+" - "+str(pointOne[1])+") mod "+str(prime)
        print "S = "+str(sn)+"/"+str(sd)+" mod "+str(prime)
        print "S = "+str(s)

    # If s > prime, must be an infinite point
    if (s > prime):
        return (0, 0)

    # Calculate and return point
    return newPoint(pointOne, pointTwo, prime, s)

# Converts int to binary, removes leading '0b' and the greatest bit
# Returns sequence as a list
def getSequence(multiple):
    if (EXAM_MODE):
        print "Double and Add sequence: " + str(bin(multiple)[2:])
    return list(bin(multiple)[3:])

def printMultiple(currentPoint, multiple):
    print str(multiple) + "P = (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) +")"

def printAddition(currentPoint):
    print"P + Q = (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")"
