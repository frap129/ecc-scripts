from gmpy2 import invert

def mod(int, p):
    if (int == p):
        return int
    elif ((int < p) and (int >= 0)):
        return int;
    else:
        return (int % p)

point = (3, 6)
prime = 17
a = 2

sn = (3 * (point[0]**2)) + a
sd = 2 * point[1]
s = prime + 1
if ((sn % sd) == 0):
    s = mod((sn//sd), prime)
else:
    s = mod((sn * invert(sd, prime)), prime)

if (s <= prime):
    print "S Value: " + str(s)
else:
    print "ya fucked up"

x = mod((((s**2) - point[0]) - point[0]), prime)
y = mod(((s * (point[0] - x)) - point[1]), prime)

print "(" + str(x) + "," + str(y) +")"
