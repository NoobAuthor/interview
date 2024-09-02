package main

import "fmt"

// Problem: Maximum Product Subarray
// Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
// which has the largest product.

func maxProduct(nums []int) int {
	res := nums[0]
	currMax, currMin := 1, 1
	for _, n := range nums {
		if n == 0 {
			currMax, currMin = 1, 1
			res = max(res, 0)
		} else {
			currMax, currMin = max(n, currMax*n, currMin*n), min(n, currMax*n, currMin*n)
			res = max(res, currMax)
		}
	}
	return res
}

func main() {
	fmt.Println(maxProduct([]int{2, 3, -2, 4})) // 6
	fmt.Println(maxProduct([]int{-2, 0, -1}))   // 0
}
