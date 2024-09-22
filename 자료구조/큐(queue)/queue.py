class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

def enqueue(self, data):
  if self.front is None:
    self.front = self.rear = Node(data)
  else:
    node = Node(data)