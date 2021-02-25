import copy
N, K = map(int, input().split())

case = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(K):
    if case[i] in plug:
        continue
    if len(plug) < N:
        plug.append(case[i])
        continue

    li = []

    for j in range(N):

        try:
            idx =case[i:].index(plug[j])
            li.append(idx)

        except:
            li.append(101)

    del plug[li.index(max(li))]
    plug.append(case[i])
    cnt += 1
            
print(cnt)
