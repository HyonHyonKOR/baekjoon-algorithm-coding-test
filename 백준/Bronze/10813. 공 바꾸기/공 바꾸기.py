basket, times_change = map(int,input().split())
arr = [i for i in range(1,basket+1)]

for _ in range(times_change):
    before, after = map(int,input().split())
    arr[before-1], arr[after-1] = arr[after-1],arr[before-1]
  
for i in range(basket):
    print(arr[i], end=' ')