# 1. 내가 짠 멋진 코드
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list_num = list(map(int, str(x)))
        for i in range(len(list_num)):
            if list_num[i] != list_num[len(list_num)-1-i]:
                return False
        return True

# 2. GPT가 짜준 더 멋진 코드
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # 음수는 팰린드롬이 될 수 없음

        # 정수를 문자열로 변환하여 팰린드롬 여부를 확인
        x_str = str(x)
        return x_str == x_str[::-1]  # 문자열을 뒤집어서 원래 문자열과 비교