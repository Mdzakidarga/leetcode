class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.split()
        if not list:
            return 0
        else:
            return len(list[-1])
        