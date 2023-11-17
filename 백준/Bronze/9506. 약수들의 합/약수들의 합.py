while True:

  num = int(input())
  result_set = set()

  if (num == -1):
    break

  else:
      for i in range(1, int(num**(1 / 2)) + 1):
          if (num % i == 0):
             result_set.add(i)
             result_set.add(num // i)

             result = sorted(result_set)
             result.pop()

      if (sum(result) == num):
          s = list(map(str, result))
          s = ' + '.join(s)
          print(f'{num} = {s}')
      else:
          print(f'{num} is NOT perfect.')