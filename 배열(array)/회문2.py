# 포인터 두 개를 이용

# 주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환

def is_palindrome(word):
  left = 0
  right = len(word)-1
  while left < right:
      if word[left] != word[right]:
          return False
      left, right = left + 1, right - 1
  return True

# Test code

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")