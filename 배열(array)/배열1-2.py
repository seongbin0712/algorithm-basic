# 0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

# 포인터 2개 이용

def bin_array_sort(arr):
  left = 0
  right = len(arr) - 1
  while left < right:
      while left < len(arr) and arr[left] == 0:
          left += 1
      while right >= 0 and arr[right] == 1:
          right -= 1
      if left < right:
          arr[left], arr[right] = 0, 1
          left, right = left + 1, right - 1

# Test code 

for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    bin_array_sort(arr)  
    print(arr)

# left가 right보다 작으면 반복
# left는 1이 나올 때까지 오른쪽으로 이동
# right는 0이 나올 때까지 왼쪽으로 이동
# left의 위치가 right의 위치보다 작으면 값을 서로 교환
# left는 오른쪽으로 한 칸, right는 왼쪽으로 한 칸 이동한다.