TC= int(input())
set = set()

for _ in range(TC):
    word = input()
    set.add(word)
  
list = list(set)
answer_list = sorted(list, key= lambda x: (len(x),x))

for i in answer_list:
    print(i)  