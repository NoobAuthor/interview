package main

import "fmt"

func fibonacci(n int) int {
	memo := map[int]int{}

	for i := 1; i <= n; i++ {
		if i <= 2 {
			memo[i] = 1
		} else {
			memo[i] = memo[i-1] + memo[i-2]
		}
	}
	return memo[n]
}

func main() {
	n := 10
	fmt.Println(fibonacci(n)) // 55
}
