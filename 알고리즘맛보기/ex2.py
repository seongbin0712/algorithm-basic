# 정수 n을 입력 받아, 1부터 n까지의 합을 구해라
# while문

n = int(input('1부터 n까지의 정수합을 구할 n을 입력하세요. : '))

sum_cnt = 0
i = 1

while i <= n:
  sum_cnt += i
  i += 1

print(f"1부터 {n}까지의 합은 {sum_cnt}입니다.")