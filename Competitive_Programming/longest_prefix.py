# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: ["flower","flow","flight"]
# Output: "fl"


class Solution:

    def longestUntil(self, str1, str2):
        common = ""
        i = 0
        j = 0
        n1 = len(str1)
        n2 = len(str2)
        while(i < n1 and j < n2):
            if(str1[i] == str2[j]):
                common += str1[i]
            else:
                break
            i += 1
            j += 1
        return common

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if(n == 0):
            return ""
        prefix = strs[0]
        for i in range(1, n):
            prefix = self.longestUntil(prefix, strs[i])

        return prefix
