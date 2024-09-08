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


if __name__ == "__main__":
    my_list = LinkedList()
    print(f"연결 리스트 생성.  연결 리스트의 길이 = {len(my_list)}")
    print()
    for i in range(4):
        my_list.appendleft(i)
        print(f"{i}을(를) 추가.  연결 리스트의 길이 = {len(my_list)}")