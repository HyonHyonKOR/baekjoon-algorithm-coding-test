students = [i + 1 for i in range(30)]

for _ in range(28):
  data = int(input())
  students.remove(data)
  
print(min(students))
print(max(students))