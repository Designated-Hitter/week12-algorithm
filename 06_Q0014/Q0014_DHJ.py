class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key = len)
        for i, char in enumerate(min_str):
            for string in strs:
                if string[i] != char:
                    return min_str[:i]
        return min_str