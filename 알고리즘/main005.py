# 정수 n을 입력 받아, 1부터 n까지의 합을 구해라
# 가우스 덧셈

n = int(input('1부터 n까지 정수합을 구할 n을 입력하세요 : '))

sum_cnt = n * ( n + 1 ) // 2

print(f"총합은 {sum_cnt}입니다.")

# n이 홀수일 경우에는, (1+n) * (n/2) + (n-(n/2))