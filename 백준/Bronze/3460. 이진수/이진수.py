n = int(input())

for _ in range(n):
    b = list(bin(int(input())))[2:]
    b.reverse()
    for j in range(len(b)):  
        if b[j] == '1':
            print(j, end = " ")  