import math

print('t | xm | ym')

for t in range(0, 21, 1):
    t = t / 10
    r = 0.1*t*t
    fi = math.pi*t/6
    xm = r*math.cos(fi)
    ym = r*math.sin(fi)
    print(f'{t} | {round(xm, 2)} | {round(ym, 2)}')
