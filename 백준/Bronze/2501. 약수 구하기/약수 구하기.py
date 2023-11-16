n,k = map(int,input().split())

a = []

for i in range(1,int(n**(1/2))+1):
    if n % i == 0: 
        a.append(i)
        if i*i != n:
            a.append(n//i)
   
a.sort()

if(k<=len(a)): print(a[k-1])
else: print(0)