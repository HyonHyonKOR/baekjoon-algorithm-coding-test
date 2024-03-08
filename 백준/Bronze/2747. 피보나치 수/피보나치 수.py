test = int(input())

if test == 0:
   print(0)
elif test == 1:
   print(1)

else:
    answer = 0
    n_1,n_2 = 0,1
    for _ in range(test-1):
        answer = n_1 + n_2
        n_1,n_2 = n_2,answer 

    print(answer)