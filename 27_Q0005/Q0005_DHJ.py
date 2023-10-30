class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        if len(s) == 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        longest = ""
        for i in range(len(s)):
            # 홀수길이 palindrome
            palindrome1 = expand(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            # 짝수길이 palindrome
            palindrome2 = expand(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest