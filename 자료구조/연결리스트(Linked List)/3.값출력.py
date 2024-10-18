# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data  # data는 값을 가리키는 변수(속성, attribute)
        self.next = None  # next는 다음 노드를 가리키는 변수

# 노드를 생성하고 연결 -> python tutor에서 확인해보기
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 연결리스트의 값 출력
node = head
while node:   # node is not None과 같은 코드
    print(node.data, end = " ")
    node = node.next

# head부터 마지막 노드까지 이동하면서 data를 출력한다.
# 이때 head는 연결 리스트의 시작이므로, head가 이동하면 연결 리스트를 잃게 된다.
# 따라서 변수(이름표)를 만들고 head부터 마지막 노드까지 이동하면서 data를 출력한다.
# 마지막 노드의 next는 None을 가리키므로, 노드가 None이 아닐 동안 계속 이동하면서 data를 출력한다.

