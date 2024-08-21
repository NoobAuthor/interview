from typing import *
# Detect a cycle in a linked list

class Node:
    def __init__(self, new_data: int):
        self.data = new_data
        self.next = None

class Solution:
    def hasCycle(self, head: Node) -> Node:
        node = set()

        while head is not None:
            if head in node:
                return True
            node.add(head)
            head = head.next
        
        return False
# Test the function
solution = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

if solution.hasCycle(head):
    print("Cycle detected")
else:
    print("No cycle detected")

