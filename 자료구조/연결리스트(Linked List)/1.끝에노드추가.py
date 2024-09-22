class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
node = head

while node.next:  # 현재 노드의 next가 None이 아닐 동안 실행
    node = node.next
node.next = Node(4)

# 변수를 만들고 head부터 마지막 노드까지 이동한다.
# 마지막 노드의 next가 새 노드를 가리키도록 한다. (next에 새 노드를 할당)