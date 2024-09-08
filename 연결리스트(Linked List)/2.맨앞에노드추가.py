class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 맨 처음에 노드 추가하기
node = Node(0)
node.next = head
head = node

# 출력해보기
node = head
while node:   #node is not None과 같은 코드
    print(node.data, end = " ")
    node = node.next
    
# 추가할 노드를 생성한다.
# 추가할 노드의 next가 head를 가리키게 한다.
# head를 추가한 노드로 옮긴다.