#1. 반복문으로 9명의 키를 입력받고 오름차순 정렬한다.
dwarfs = [int(input()) for _ in range(9)]
real_dwarfs = sorted(dwarfs)

#2. 순열과 조합처럼 9개의 배열 중 2명의 조합을 선택한 후, 
#  (배열의 총합 - 2명의 조합)이 100인지 확인한다.

sum_dwarfs = sum(real_dwarfs)

is_seven_dwarfs = False
for i in range(9):
  #j는 상수를 넣으면 중복수가 발생하므로 변수로 처리한다
      for j in range(i+1,9):
        #가짜를 찾으면 복사한 배열에서 그 가짜 요소 두개만 제거한다
         if sum_dwarfs - (dwarfs[i] + dwarfs[j]) == 100:
              real_dwarfs.remove(dwarfs[i])
              real_dwarfs.remove(dwarfs[j])
              is_seven_dwarfs = True
              break

      if is_seven_dwarfs == True:
          break

for dwarf in real_dwarfs:
    print(dwarf)