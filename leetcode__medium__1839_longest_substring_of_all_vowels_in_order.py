# https://leetcode.com/contest/weekly-contest-238/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        word += 'a'
        o = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        l = 0
        maxlen = 0
        elements = {word[0]}
        for r in range(1, len(word)):
            if o[word[r]] - o[word[r-1]] not in [0, 1]:
                if len(elements) == 5 and r-l > maxlen: 
                    maxlen = r-l
                l = r
                elements = set()
            elements.add(word[r])

        # if len(elements) == 5 and r-l > maxlen:
        #     maxlen = r-l
        return maxlen