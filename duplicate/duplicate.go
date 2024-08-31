package main

func duplicate(nums []int) bool {
	hash := map[int]bool{}

	for _, n := range nums {
		if _, ok := hash[n]; ok {
			return true
		}
		hash[n] = true
	}
	return false
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	println(duplicate(nums)) // false
}
