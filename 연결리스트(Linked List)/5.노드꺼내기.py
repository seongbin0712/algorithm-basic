# Node를 생성하는 Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트를 생성/관리하는 Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if node == self.head:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return node.data

if __name__ == "__main__":
    import random
    data = list(range(10, 15))
    random.shuffle(data)
    my_list = LinkedList()
    for i in data:
        my_list.appendleft(i)
    print(f"연결 리스트의 상태\n{my_list}")
    print()
    for _ in range(len(my_list)):
        print(f"{my_list.pop()}를(을) 꺼낸 후: 길이 = {len(my_list)}, {my_list}")
    print(f"연결 리스트가 비었을 때 꺼낸 값은 {my_list.pop()}")