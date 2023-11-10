import sys

range_num = int(sys.stdin.readline().rstrip())

for i in range(range_num):
    print(' '*(range_num-(i+1))+'*'*(i+1))