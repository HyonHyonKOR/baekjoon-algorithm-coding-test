def find_self_num(n):
    not_selfnum = []
    for i in range(n):
        digit_sum = 0
        for j in str(i):
            digit_sum += int(j)

        not_selfnum.append(i+digit_sum)
        digit_sum=0

    not_selfnum_set = set(not_selfnum)
    not_selfnum = list(not_selfnum_set)
    not_selfnum.sort()

    for k in range(1,n):
        if k not in not_selfnum:
          print(k)



find_self_num(10000)