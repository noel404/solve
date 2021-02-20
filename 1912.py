import sys
i = int(input())
li = list(map(int, sys.stdin.readline().split()))
a = [0] * i
a[0] = li[0]
for k in range(1, i):
    a[k] = max(li[k], li[k]+a[k-1])

print(max(a))
