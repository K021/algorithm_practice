# https://leetcode.com/contest/weekly-contest-238/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print("nums:", [(i, n) for i, n in enumerate(nums)])

        cnts = [1] * len(nums)
        l, o, r, diff = 0, 0, 0, nums[0]
        bullet = k
        # print("cnts:", cnts)
        while r < len(nums):
            # print("l, r:", l, r, "cnts[r]:", cnts[r], "bullet:", bullet, "diff:", diff)
            # print("l, r:", l, r, "cnts:", cnts, "bullet:", bullet, "diff:", diff)
            if cnts[r] == r - l + 1:
                r += 1
                if r < len(nums): diff = nums[r] - nums[r-1]
                while not diff and r < len(nums):
                    cnts[r] += cnts[r-1]
                    r += 1
                    if r < len(nums): diff = nums[r] - nums[r-1]
                o = r
            elif bullet >= diff:
                cnt = min(bullet // diff, o-l)
                bullet -= cnt * diff
                cnts[r] += cnt
                o -= cnt
            elif l < o:
                bullet += nums[r-1] - nums[l]
                # print(f"<move l> bullet={bullet}, nums[r-1]={nums[r-1]}, l={l}")
                l += 1

        # print(cnts)
        return max(cnts)

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1
        nums.sort()
        # print("nums:", [(i, n) for i, n in enumerate(nums)])

        cnts = [1] * len(nums)
        l, r, diff = 0, 1, nums[0]
        bullet = k
        # print("cnts:", cnts)
        while r < len(nums):
            
            cnts[r] += cnts[r-1]  # r renewals every loop
            diff = nums[r] - nums[r-1]
            
            # print(cnts)
            # print(f"l={l}, r={r}", "cnts[r]:", cnts[r], "bullet:", bullet, "diff:", diff)
            # print("l, r:", l, r, "cnts:", cnts, "bullet:", bullet, "diff:", diff)
            
            bullet -= diff * (r-l)
            while bullet < 0:
                # print('while loop:', 'bullet', bullet, f'l={l}, r={r}', 'nums[r]:', nums[r], 'nums[l]', nums[l])
                bullet += nums[r] - nums[l]
                l += 1
                cnts[r] -= 1
            r += 1

        # print(cnts)
        return max(cnts)

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        maxi = cnt = 0
        l, r = 0, 0
        while r < len(nums):
            cnt += 1  # r renewals every loop

            k -= (nums[r] - nums[r-1]) * (r-l) if r else 0
            while k < 0:
                k += nums[r] - nums[l]
                l += 1
                cnt -= 1
            if cnt > maxi: maxi = cnt
            r += 1

        return maxi
