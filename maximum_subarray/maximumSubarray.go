package main

func maximumSubarray(nums []int) int {
	maxSum := nums[0]
	currentSum := nums[0]

	for i := 1; i < len(nums); i++ { // start from 1 because we already have the first element
		if currentSum < 0 { // if the current sum is negative, we reset it to 0
			currentSum = 0
		}
		currentSum += nums[i]            // add the current number to the current sum
		maxSum = max(maxSum, currentSum) // update the max sum
	}
	return maxSum
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}

	println(maximumSubarray(nums)) // 6
}
