import sys
x, l, r = map(int, sys.stdin.readline().split())
mm = abs(x-l)
m = l
for i in range(l, r+1):
    new = abs(x - i)
    if mm > new:
        mm = new
        m = i
        

print(m)
