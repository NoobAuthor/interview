from typing import *

# Given a linked list and an integer N, the task is to delete the Nth node from the end of the given linked list.

class Node:
    def __init__(self, new_data: int):
        self.data = new_data
        self.next = None

class Solution:
    def removeNode(self, head: Node, N: int) -> Node:
        # First, we need to find the length of the linked list
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        
        # If the N is greater than the length of the linked list, then return the head
        if N > length:
            return head
        
        # If the N is equal to the length of the linked list, then return the head.next
        if N == length:
            return head.next
        
        # Otherwise, we need to find the (length - N)th node from the beginning
        temp = head
        for i in range(1, length - N):
            temp = temp.next
        
        # Remove the Nth node from the end
        temp.next = temp.next.next
        
        return head

# Test the function
solution = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

N = 2
result = solution.removeNode(head, N)
while result is not None:
    print(result.data, end = " ")
    result = result.next

print()