# 정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 
# 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)

# 포인터 2개 이용

def find_sub_array(arr, s):
    left = 0
    sub_total = 0
    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]


# Test code
sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
sample3 = ([1, 2, 3, 4], 0)
for arr, s in (sample1, sample2, sample3):
    print(find_sub_array(arr, s))

# left와 right라는 포인터를 만든다.
# right를 오른쪽으로 이동하면서, right 위치의 배열 원소를 더한다.
# 더한 값이 S보다 작으면 right를 증가시키고 배열의 원소를 더한다.
# 더한 값이 S보다 크면 S와 같거나 작아질 때까지 left 위치의 원소를 뺀다.
# 더한 값이 S이면 (left+1, right+1)을 반환한다.
# 마지막 원소까지 갔을 때 S와 같은 값이 없으면 [-1]을 반환한다.