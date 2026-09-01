# Lab ระหว่างเรียน ส่วนที่ 3: Doubly และ Circular Linked List

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_forward(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.next
    print("null")

def traverse_backward(tail):
    currentNode = tail
    while currentNode:
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.prev
    print("null")

def traverse_circular_singly(head):
    if not head:
        print("null")
        return

    startNode = head
    currentNode = head
    while True:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
        if currentNode == startNode:
            break
    print("null")

def traverse_circular_doubly_forward(head):
    if not head:
        print("null")
        return

    startNode = head
    currentNode = head
    while True:
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.next
        if currentNode == startNode:
            break
    print("null")

def traverse_circular_doubly_backward(tail):
    if not tail:
        print("null")
        return

    startNode = tail
    currentNode = tail
    while True:
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.prev
        if currentNode == startNode:
            break
    print("null")

print("--- ผลลัพธ์ส่วนที่ 3: Doubly & Circular ---")
print("\nทดสอบ Doubly Linked List:")

dnode1 = DoublyNode(3)
dnode2 = DoublyNode(5)
dnode3 = DoublyNode(13)

dnode1.next = dnode2
dnode2.prev = dnode1
dnode2.next = dnode3
dnode3.prev = dnode2

print("Traverse forward:")
traverse_forward(dnode1)
print("Traverse backward:")
traverse_backward(dnode3)

print("\nทดสอบ Circular Singly Linked List:")
cnode1 = Node(3)
cnode2 = Node(5)
cnode3 = Node(13)

cnode1.next = cnode2
cnode2.next = cnode3
cnode3.next = cnode1

print("Traverse circular singly forward:")
traverse_circular_singly(cnode1)

print("\nทดสอบ Circular Doubly Linked List:")
cdnode1 = DoublyNode(3)
cdnode2 = DoublyNode(5)
cdnode3 = DoublyNode(13)
cdnode4 = DoublyNode(2)

cdnode1.next = cdnode2
cdnode2.prev = cdnode1
cdnode2.next = cdnode3
cdnode3.prev = cdnode2
cdnode3.next = cdnode4
cdnode4.prev = cdnode3

cdnode4.next = cdnode1
cdnode1.prev = cdnode4

print("Traverse circular doubly forward:")
traverse_circular_doubly_forward(cdnode1)
print("Traverse circular doubly backward:")
traverse_circular_doubly_backward(cdnode3)