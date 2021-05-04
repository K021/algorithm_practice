# https://leetcode.com/contest/weekly-contest-237/problems/find-xor-sum-of-all-pairs-bitwise-and/
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor = lambda x, y: x ^ y
        return reduce(xor, arr1) & reduce(xor, arr2)