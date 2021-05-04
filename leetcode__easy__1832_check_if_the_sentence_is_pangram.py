# https://leetcode.com/contest/weekly-contest-237/problems/check-if-the-sentence-is-pangram/
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26