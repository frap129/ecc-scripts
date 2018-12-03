from gmpy2 import invert

def mod(int, p):
    if (int == p):
        return int
    elif ((int < p) and (int >= 0)):
        return int;
    else:
        return (int % p)

x1 = 5
y1 = 1
x2 = 8
y2 = 7
a = 2
p = 17

sn = (y2 - y1)
sd = (x2 - x1)
s = p + 1
if ((sn % sd) != 0):
    s = mod((sn * invert(sd, p)), p)
else:
    s = mod((sn//sd), p)

if (s < p):
    print s
else:
    print "ya messed up"

x3 = mod((((s^2) - x1) - x2), p)
y3 = mod(((s * (x1 - x3)) - y1), p)

print "(" + str(x3) + "," + str(y3) + ")"
