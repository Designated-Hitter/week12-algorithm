class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else :
                if not stack:
                    return False
                top = stack.pop()
                if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "["):
                    return False
        if stack != []:
            return False
        return True