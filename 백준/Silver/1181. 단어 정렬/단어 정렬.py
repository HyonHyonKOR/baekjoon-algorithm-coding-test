test_case = int(input())
before_sort = [input() for _ in range(test_case)]

before_sort_set = set(before_sort)
before_sort = list(before_sort_set)

after_sort = sorted(before_sort)
after_sort.sort(key =len)

for i in after_sort:
    print(i)