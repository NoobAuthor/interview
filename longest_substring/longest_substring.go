package main

import "fmt"

func longest_substring(s string) int {
	if len(s) == 0 {
		return 0
	}
	l, r := 0, 0
	res := 0
	seen := map[byte]int{}

	for r < len(s) {
		if _, ok := seen[s[r]]; ok {
			l = max(l, seen[s[r]]+1)
		} else {
			res = max(res, r-l+1)
		}
		seen[s[r]] = r
		r++
	}
	return res
}

func main() {
	s := "abcabcbb"
	fmt.Println(longest_substring(s))
}
