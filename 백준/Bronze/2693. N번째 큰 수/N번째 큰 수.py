TC = int(input())

for _ in range(TC):
    A = list(map(int,input().split()))
    A.sort()
    print(A[-3])
    del A