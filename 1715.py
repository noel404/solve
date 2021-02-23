import sys, heapq

N=int(input())
li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))

su = 0
heapq.heapify(li)

while len(li)!=1:
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    su += (a+b)
    heapq.heappush(li, a+b)

print(su)
