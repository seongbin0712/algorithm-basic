# 회문 : 앞 뒤로 읽을 때 단어의 순서가 같은 단어를 의미한다.
# 문자열의 슬라이싱을 이용

# 주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환

word = "racecar"

if word == word[::-1]:
  print(True)
else:
  print(False)

# ex) racecar, madam은 회문, tomato는 회문이 아니다.