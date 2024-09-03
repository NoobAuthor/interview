package main

import "fmt"

// Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

// Definition for singly-linked list.
type Node struct {
	Val  int
	Next *Node
}

func mergeTwoLists(l1 *Node, l2 *Node) *Node {
	// Create a dummy node to hold the merged list
	dummy := &Node{}
	// Create a pointer to the dummy node
	current := dummy

	// While both lists are not empty
	for l1 != nil && l2 != nil {
		// If the value of l1 is less than the value of l2
		if l1.Val < l2.Val {
			// Set the next node of the current node to the value of l1
			current.Next = l1
			// Move to the next node in l1
			l1 = l1.Next
		} else {
			// Set the next node of the current node to the value of l2
			current.Next = l2
			// Move to the next node in l2
			l2 = l2.Next
		}
		// Move to the next node in the merged list
		current = current.Next
	}

	// If there are any remaining nodes in l1 or l2
	if l1 != nil {
		// Set the next node of the current node to the remaining nodes in l1
		current.Next = l1
	} else {
		// Set the next node of the current node to the remaining nodes in l2
		current.Next = l2
	}

	// Return the merged list
	return dummy.Next
}

func main() {
	// Create two sorted linked lists
	l1 := &Node{Val: 1, Next: &Node{Val: 3, Next: &Node{Val: 5}}}
	l2 := &Node{Val: 2, Next: &Node{Val: 4, Next: &Node{Val: 6}}}

	// Merge the two lists
	merged := mergeTwoLists(l1, l2)

	// Print the merged list
	for merged != nil {
		fmt.Printf("%d ", merged.Val)
		merged = merged.Next
	}
	fmt.Println()
}
