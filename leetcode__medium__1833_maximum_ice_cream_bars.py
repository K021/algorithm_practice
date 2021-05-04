# https://leetcode.com/contest/weekly-contest-237/problems/maximum-ice-cream-bars/
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = [0] + sorted(costs)
        for i in range(len(costs)-1):
            costs[i+1] += costs[i]
            if costs[i+1] > coins: return i
        return len(costs)-1