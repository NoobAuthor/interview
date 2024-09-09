package main

import (
	"fmt"
)

//  Problem: Minimum Coins
//  Given a list of coin denominations and a target sum of money,
//  find the minimum number of coins needed to make up the target sum.

func minimuCoins(coins []int, target int) int {
	// create a slice to store the minimum number of coins needed to make up the target sum
	minCoins := make([]int, target+1)

	// initialize the slice with a large number
	for i := 1; i <= target; i++ {
		minCoins[i] = target + 1
	}

	// iterate through the coins
	for _, coin := range coins {
		// iterate through the target sum
		for i := coin; i <= target; i++ {
			// check if the current coin can be used to make up the target sum
			if minCoins[i-coin]+1 < minCoins[i] {
				minCoins[i] = minCoins[i-coin] + 1
			}
		}
	}

	// return the minimum number of coins needed to make up the target sum
	if minCoins[target] > target {
		return -1
	}
	return minCoins[target]
}

func main() {
	coins := []int{1, 3, 4}
	target := 6
	result := minimuCoins(coins, target)
	fmt.Println(result) // Output: 2
}
