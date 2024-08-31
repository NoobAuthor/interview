package main

// Detect a cycle in a linked list

type Node struct {
	data int
	next *Node
}

func detectCycle(head *Node) bool {
	// create a set/map to store the node
	node := map[*Node]bool{}

	for head != nil {
		// if head in node
		if _, ok := node[head]; ok {
			return true
		}
		node[head] = true // add head to node
		head = head.next
	}
	return false
}

func main() {
	head := &Node{data: 1}
	head.next = &Node{data: 2}
	head.next.next = &Node{data: 3}
	head.next.next.next = &Node{data: 4}
	head.next.next.next.next = head.next

	if detectCycle(head) {
		println("Cycle detected")
	} else {
		println("Cycle not detected")
	}
}
