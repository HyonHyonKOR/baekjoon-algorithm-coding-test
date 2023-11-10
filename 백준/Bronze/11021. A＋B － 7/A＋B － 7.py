import sys

for i in range(int(sys.stdin.readline().rstrip())):
  num1, num2 = map(int, sys.stdin.readline().split())
  print(f"Case #{i+1}: {num1 + num2}")