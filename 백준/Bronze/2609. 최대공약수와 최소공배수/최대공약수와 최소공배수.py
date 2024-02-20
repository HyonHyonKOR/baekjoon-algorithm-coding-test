# 최대 공약수와 최소 공배수
def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a     

def lcm(a,b):
    return a*b // gcd(a,b)

x,y = map(int,input().split())

#x가 y보다 큰 경우 
if x>=y: 
    print(gcd(x,y))
    print(lcm(x,y))
#y가 큰 경우
else: 
    print(gcd(y,x))
    print(lcm(y,x))