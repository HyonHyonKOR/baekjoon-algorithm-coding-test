nth_fivo = int(input())
fivo_before_before = 0
fivo_before = 1

if nth_fivo == 0:
  print(0)
elif nth_fivo == 1:
  print(1)
else:
  result = 0
  for _ in range(nth_fivo - 1):
    result = fivo_before_before + fivo_before
    fivo_before_before = fivo_before
    fivo_before = result

  print(result)