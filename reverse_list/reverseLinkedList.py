from typing import * 

# Reverse a singly linked list

class Node:
    def __init__(self, new_data: int):
        self.data = new_data
        self.next = None

class Solution:
    def reverseList(self, head: Node) -> Node:
        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

def printList(head: Node):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Test the function 
solution = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
printList(head)
head = solution.reverseList(head)
print("Reversed list:")
printList(head)  # Output should be 5 4 3 2 1