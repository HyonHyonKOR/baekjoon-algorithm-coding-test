train = []

for i in range(10):
    a,b = map(int,input().split())
    if i == 0:
        train.append(b-a)
    elif i< 8:
        train.append(b-a+ train[i-1])
    else:
        train.append(train[-1]-b)

print(max(train))