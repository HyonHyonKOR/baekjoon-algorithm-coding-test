length= int(input())
length_arr = list(map(int,input().split()))
length_arr.sort()

print(length_arr[0],length_arr[-1])