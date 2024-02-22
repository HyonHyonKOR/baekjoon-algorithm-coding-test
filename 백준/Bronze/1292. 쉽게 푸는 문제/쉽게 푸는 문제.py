#1. 수열을 만든다
list = []

for i in range(1,100):
    for _ in range(i):
        list.append(i)
        
    if len(list)==1000:
        break

#2. 입력을 받는다
start,finish = map(int,input().split())

#3. 배열을 슬라이스 후 답을 출력한다
print(sum(list[start-1:finish]))