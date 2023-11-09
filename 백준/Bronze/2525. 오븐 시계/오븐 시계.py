now_h, now_m = map(int, input().split())
cook_t = int(input())

result_m = (now_m + (cook_t % 60)) % 60  
result_h = now_h + (cook_t // 60) + ((now_m + (cook_t % 60)) // 60)

if (result_h < 23):
  print(result_h, result_m)
else:
  print(result_h % 24, result_m)