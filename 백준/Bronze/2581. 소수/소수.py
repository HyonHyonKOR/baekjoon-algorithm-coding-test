# 두 수 사이의 소수 구하기

start_num = int(input())
finish_num = int(input())
prime_list = []

for num in range(start_num, finish_num+1):
    if num < 2:
        continue
  
    for i in range(2,int(num**(1/2))+1):      
        if num % i == 0:
            break
          
    else:
        prime_list.append(num)    
    

if len(prime_list) > 0:
    print(sum(prime_list))
    print(prime_list[0])

else:
    print(-1)