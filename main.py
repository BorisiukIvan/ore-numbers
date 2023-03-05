# You should create a special file named "ore" and write there some ore numbers (ex. 6, 28, 496, 6200 and 8128)
def stF(x, i):
    res = 0
    while i >= 0:
          res = res + x**i 
          i = i - 1
    return res

def multiply_num(x0, f0, y):
    f = f0[:]
    s = 1
    n = 1
    x = x0
    i = 5
    for k in range(0, len(f)): f[k] = int(f[k])
    if (y % 2 == 0) and (2 not in f): f.append(2)
    if (y % 3 == 0) and (3 not in f): f.append(3)
    while (y % 3 == 0): y = y / 3
    while (y % 2 == 0): y = y / 2
    k = 1
    while y > 1:
         while (y % i):
             if (k):
                i = i + 2
             else: i = i + 4
             k = (k + 1) % 2
             if (i * i > x): i = y
         if (i not in f): f.append(i)
         y = y / i

    for i in f:
        m = 1
        while (x%i == 0):
            x = x / i
            m = m + 1
        if (m > 1):
            n = n * m
            s = s * stF(i, m-1)
    for k in range(0, len(f)): f[k] = str(f[k])
    if ( (x0 * n) % s == 0): return str(x0) + " MN " + ":".join(f)
    return '0'

b = 6
k = 1
c = 0

# You can set your value, if you want.
p = 10000

arr = open("ore").read().split("\n")
arr2 = []
for i in arr:
    if (not i): continue
    arr2.append(int(i.split(" ")[0]))

for s in arr:
    if (not s): continue
    n = int(s.split(" ")[0])
    f = s.split("MN ")[1].split(":")
    if (n == b): k = 1
    if (not k): continue
    c = c + 1
    if (c % 100 == 0): open("ore_log", "w").write(str(n) + " " + str(c))
    for i in range(2, p):
        if (not n*i): continue
        y = multiply_num(n*i, f, i)
        t = int(y.split(" ")[0])
        if (t) and (t not in arr2):
            print t, "NUM", i
            open("ore", "a").write(y + "\n")
            arr.append(y)
            arr2.append(t)
