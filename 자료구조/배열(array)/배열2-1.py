# 정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 
# 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)

# 이중 반복문 사용

def find_sub_array(arr, s):
    for i in range(len(arr)):
        sub_total = 0
        for j in range(i, len(arr)):
            sub_total += arr[j]
            if sub_total == s:
                return [i+1, j+1]
    return [-1]

# Test code
sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)

for arr, s in (sample1, sample2):
    print(find_sub_array(arr, s))

# i는 인덱스 0부터 마지막 인덱스까지 반복한다.
# 부분 배열의 합을 0으로 초기화한다.
# j는 i부터 마지막 인덱스까지 반복한다.
# 배열의 값을 더한다.
# 누적한 값이 제시된 값과 같으면 인덱스를 반환한다.
# 반복문을 빠져 나오면 답이 없으므로 –1을 반환한다.