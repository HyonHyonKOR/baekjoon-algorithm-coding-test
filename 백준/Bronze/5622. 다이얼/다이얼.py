alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
result = 0

for i in word:
    for j in alpabet:
        if i in j:
            result += (alpabet.index(j) + 3)

print(result)