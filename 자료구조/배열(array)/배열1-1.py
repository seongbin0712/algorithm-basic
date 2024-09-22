# 0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

# count 메서드 이용

def bin_array_sort(arr):
  arr[:] = [0] * arr.count(0) + [1] * arr.count(1)


# Test code

for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    bin_array_sort(arr)  
    print(arr)

# 0과 1만 있으므로, count() 메서드를 이용하여 0과 1의 개수를 센다.
# 해당 개수만큼 0과 1을 채운다.