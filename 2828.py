import sys
def solve():
    N, M = map(int, sys.stdin.readline().split())
    J = int(sys.stdin.readline())
    case = [int(sys.stdin.readline()) for _ in range(J)]
    basket = (range(1,M+1))
    k = 0
    cnt = 0
    for i in range(J):
        while case[i] not in basket:
            if case[i] > max(basket):
                k += 1
                basket = (range(1+k,M+1+k))
                cnt += 1
            else:
                k -= 1
                basket = (range(1+k,M+1+k))
                cnt += 1


    print(cnt)
            
solve()
