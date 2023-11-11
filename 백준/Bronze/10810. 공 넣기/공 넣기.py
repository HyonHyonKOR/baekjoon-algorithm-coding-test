len, repeat_time = map(int, input().split())
arr = [0] * len

for i in range(repeat_time):
  start, end, element = map(int, input().split())
  for j in range(start - 1, end):
    arr[j] = element

for i in range(len):
  print(arr[i], end=' ')