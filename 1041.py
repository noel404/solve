import copy
def solve():
    N = int(input())
    a,b,c,d,e,f = map(int,input().split())
    t_case = [(a+b+c),(a+e+c), (a+e+d),(a+d+b),(f+d+e),(f+c+e),(f+b+c),(f+d+b)]
    o_case = [a,b,c,d,e,f]
    d_case = []
    for i in range(6):
        for j in range(6):
            li = copy.copy(o_case)
            li[-(i+1)] = None
            if i==j:
                continue
            if li[i] is None or li[j] is None:
                continue
            pair = li[i]+li[j]
            d_case.append(pair)
            
    if N == 1:
        o = []
        for i in range(6):
            li = copy.copy(o_case)
            li[i] = 0
            o.append(sum(li))

        print(min(o))
        return

    t_min = min(t_case)
    d_min = min(d_case)
    o_min = min(o_case)
    
    t = 4
    d = 4*(N-2)+4*(N-1)
    A = 5*(N**2)
    o = (A - ((3*t) + (2*d)) if N > 2 else 0)

    cnt = (t_min*t) + (d_min*d) + (o_min*o)
    print(cnt)

solve()
