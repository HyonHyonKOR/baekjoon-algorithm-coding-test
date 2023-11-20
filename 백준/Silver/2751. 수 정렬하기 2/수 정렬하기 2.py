import sys

n = int(sys.stdin.readline().rstrip())
arr = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
for i in arr:
    print(i)