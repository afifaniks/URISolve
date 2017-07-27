from sys import stdin

for s in stdin:
    s = s.split()[0]
    if len(s) == 0 or s == '0':
        break

    gg = len(s)

    ctr = 1

    while gg>0:
        ctr*=gg
        gg-=1

    print(ctr)

