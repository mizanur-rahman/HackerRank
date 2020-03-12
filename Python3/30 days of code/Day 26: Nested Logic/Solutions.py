ad, am, ay = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ay > ey):
    print(10000)
elif (am, ay)==(em, ey) and (ad > ed):
    print(15*(ad-ed))
elif (ay == ey) and (am > em):
    print(500 * (am - em))
else:
    print(0)
