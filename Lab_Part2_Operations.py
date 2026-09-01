# Lab ระหว่างเรียน ส่วนที่ 2: การดำเนินการกับลิสต์ (Operations)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_singly(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next

    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next
    return head

print("--- ผลลัพธ์ส่วนที่ 2: Operations ---")

node1 = Node(9)
node2 = Node(1)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print("ค่าที่น้อยที่สุด:", findLowestValue(node1))

newNode = Node(98)
node1 = insertNodeAtPosition(node1, newNode, 3)
print("\nหลังแทรก 98 ตำแหน่งที่ 3:")
traverse_singly(node1)

node1 = deleteSpecificNode(node1, node2) # ลบโหนดที่มีค่า 1 (node2)
print("\nหลังลบโหนดที่มีค่า 1:")
traverse_singly(node1)
