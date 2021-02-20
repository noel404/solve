i = int(input())
a = []
ca = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0]
for k in range(4, 12):
    ca[k] = ca[k-1] + ca[k-2] + ca[k-3]

for _ in range(i):
    a.append(int(input()))

for k in a:
    print(ca[k])
