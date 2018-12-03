from gmpy2 import invert


# Needed values
pointOne = (5, 1)
pointTwo = (6, 3)
prime = 17

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
    else:
        print "s value: " + str(s)

    return s

# Calculate a point addition
def newPoint(pointOne, pointTwo, prime, s):
    x = mod((((s**2) - pointOne[0]) - pointTwo[0]), prime)
    y = mod(((s * (pointOne[0] - x)) - pointOne[1]), prime)
    return (x, y)

# Calculate s value for addition and add
def add(pointOne, pointTwo, prime):
    # Calculate s value
    sn = (pointTwo[1] - pointOne[1])
    sd = (pointTwo[0] - pointOne[0])
    s = sValue(sn, sd, prime)

    # Calculate and return point
    return newPoint(pointOne, pointTwo, prime, s)

sumPoint = add(pointOne, pointTwo, prime)
print"P+Q = (" + str(sumPoint[0]) + "," + str(sumPoint[1]) + ")"

