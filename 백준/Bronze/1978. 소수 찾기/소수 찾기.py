loop = int(input())
unchecked_list = list(map(int,input().split()))

prime_count = 0
for i in unchecked_list:
    if i < 2:
          continue
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            break
    else: 
          prime_count += 1

print(prime_count)