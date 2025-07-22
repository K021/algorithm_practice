# https://leetcode.com/contest/weekly-contest-238/problems/sum-of-digits-in-base-k/

class Solution:
    def change_base(self, num: int, base: int) -> list[int]:
        q, r = divmod(num, base)
        return [r] if not q else self.change_base(q, base) + [r]
    def sumBase(self, n: int, k: int) -> int:
        return sum(self.change_base(n, k))