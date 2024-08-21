from typing import *

# Merge two sorted linked lists

class Node:
    def __init__(slef, new_data: int):
        slef.data = new_data
        slef.next = None

class Solution:
    def merge_sort_list(self, a: Node, b: Node) -> Node:
        if a is None:
            return b
        elif b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.merge_sort_list(a.next, b)
        else:
            result = b
            result.next = self.merge_sort_list(a, b.next)
        
        return result
    
# Test the function
solution = Solution()
a = Node(1)
a.next = Node(3)
a.next.next = Node(5)
a.next.next.next = Node(7)
a.next.next.next.next = Node(9)

b = Node(2)
b.next = Node(4)
b.next.next = Node(6)
b.next.next.next = Node(8)
b.next.next.next.next = Node(10)

result = solution.merge_sort_list(a, b)
while result is not None:
    print(result.data, end = " ")
    result = result.next
print()

