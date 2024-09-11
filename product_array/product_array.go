package main

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))
	res[0] = 1
	left_product := 1

	for i := 1; i < len(nums); i++ {
		left_product *= nums[i-1]
		res[i] = left_product
	}

	for i := len(nums) - 2; i >= 0; i-- {
		res[i] *= nums[i+1]
		nums[i] *= nums[i+1]
	}

	return res
}

func main() {
	nums := []int{1, 2, 3, 4}
	productExceptSelf(nums)
}
