class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        answer = 0
        substring = []

        for character in s:
            if character not in substring:
                substring.append(character)
            else:
                answer = max(answer, len(''.join(substring)))
                replace_index = substring.index(character)
                substring = substring[replace_index + 1 : ]
                substring.append(character)

        answer = max(answer, len(substring))
        return answer