length, min_num = map(int, input().split())
length_arr = list(map(int,input().split()))

for i in range(length):
    if length_arr[i] < min_num:
        print(length_arr[i], end=' ')