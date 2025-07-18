class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        strs.sort(key=lambda x:len(x))
        for i in range(len(strs[0])):
            c = map(lambda x:x[i] == strs[0][i], strs)
            if all(c):
                output += strs[0][i]
            else:
                return output
        return output 